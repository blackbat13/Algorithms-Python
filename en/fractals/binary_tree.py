import turtle


def binary_tree(rank: int, length: float):
    turtle.forward(length)
    if rank > 0:
        turtle.left(45)
        binary_tree(rank - 1, length / 2)
        turtle.right(90)
        binary_tree(rank - 1, length / 2)
        turtle.left(45)
    turtle.back(length)


turtle.speed(0)
turtle.penup()
turtle.left(90)
turtle.back(350)
turtle.pendown()
turtle.pensize(3)
binary_tree(5, 400)
turtle.done()