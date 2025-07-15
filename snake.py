from turtle import Turtle,Screen
position = [(0,0),(-20,0), (-40,0)]
distance = 20
up = 90
down = 270
right = 0
left = 180

class Snake():
    def __init__(self):
        self.snake_part = []
        self.create_snake()
        self.snake_head = self.snake_part[0]

    def create_snake(self):
        for p in position:
            self.snake_body(p)

    def snake_body(self,position):
        my_turtle = Turtle(shape="square")
        my_turtle.penup()
        my_turtle.color("white")
        my_turtle.goto(position)
        self.snake_part.append(my_turtle)

    def extend(self):
        self.snake_body(self.snake_part[-1].position())

    def snake_move(self):
        for snake in range(len(self.snake_part) - 1, 0, -1):
            new_x = self.snake_part[snake - 1].xcor()
            new_y = self.snake_part[snake - 1].ycor()
            self.snake_part[snake].goto(x=new_x, y=new_y)
        self.snake_part[0].forward(distance)

    def up(self):
        if self.snake_head.heading() != down:
            self.snake_head.setheading(up)

    def down(self):
        if self.snake_head.heading() != up:
            self.snake_head.setheading(down)

    def right(self):
        if self.snake_head.heading() != left:
            self.snake_head.setheading(right)

    def left(self):
        if self.snake_head.heading() != right:
            self.snake_head.setheading(left)