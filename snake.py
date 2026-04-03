from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_square(position)

    def add_square(self, position):
            square = Turtle()
            square.penup()
            square.goto(position)
            square.shape("square")
            square.color("white")
            self.snake.append(square)

    def extend_snake(self):
        self.add_square(self.snake[-1].position())

    def reset_snake(self):
        for square in self.snake:
            square.goto(1000,1000)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]

    def move(self):
        for square_number in range(len(self.snake) - 1, 0, -1):
            previous_x = self.snake[square_number - 1].xcor()
            previous_y = self.snake[square_number - 1].ycor()
            self.snake[square_number].goto(previous_x, previous_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)