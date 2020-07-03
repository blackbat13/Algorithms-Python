import turtle


def koch_curve(rank: int, length: float) -> None:
    if rank > 0:
        koch_curve(rank - 1, length / 2)
        turtle.left(60)
        koch_curve(rank - 1, length / 2)
        turtle.right(120)
        koch_curve(rank - 1, length / 2)
        turtle.left(60)
        koch_curve(rank - 1, length / 2)
    else:
        turtle.forward(length)


turtle.speed(0)
turtle.penup()
turtle.back(350)
turtle.pendown()
koch_curve(3, 200)
turtle.done()
