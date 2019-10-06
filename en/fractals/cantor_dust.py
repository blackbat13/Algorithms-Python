import turtle


def cantor_dust(rank: int, length: float):
    if rank > 0:
        cantor_dust(rank - 1, length / 3)
        turtle.penup()
        turtle.forward(length / 3)
        turtle.pendown()
        cantor_dust(rank - 1, length / 3)
    else:
        turtle.forward(length)


def cantor(rank: int, length: float):
    for i in range(0, rank + 1):
        cantor_dust(i, length)
        turtle.penup()
        turtle.back(length)
        turtle.right(90)
        turtle.forward(20)
        turtle.left(90)
        turtle.pendown()


turtle.speed(0)
turtle.penup()
turtle.back(250)
turtle.pendown()
cantor(5, 500)
turtle.hideturtle()
turtle.done()
