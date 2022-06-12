from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

def move_forward():
    turtle.forward(10)
def move_backward():
    turtle.backward(10)
def turn_left():
    turtle.left(7)
def turn_right():
    turtle.right(7)

screen.listen()
screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=move_backward, key="s")
screen.onkey(fun=turn_left, key="a")
screen.onkey(fun=turn_right, key="d")

screen.exitonclick()
