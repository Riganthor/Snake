from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(1)
        self.color("white")
        self.penup()
        self.goto(0,0)
        self.x_move = 10
        self.y_move = 10
        self.speed("fastest")
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

        if self.ycor() > 280 or self.ycor() < -280:
            self.bounce_y()

    def bounce_y(self):
        # Bounce the ball when it hits the top or bottom wall.
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()

