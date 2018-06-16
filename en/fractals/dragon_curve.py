import turtle


def dragon_curve(rank, sign, length):
    if rank > 0:
        turtle.left(45 * sign)
        dragon_curve(rank - 1, 1, length)
        turtle.right(90 * sign * -1)
        dragon_curve(rank - 1, -1, length)
        turtle.left(45 * sign)
    else:
        turtle.forward(length)


turtle.speed(0)
turtle.penup()
turtle.back(150)
turtle.left(90)
turtle.forward(150)
turtle.right(90)
turtle.pendown()
dragon_curve(10, 1, 5)
turtle.done()
