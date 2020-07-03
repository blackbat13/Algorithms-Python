import turtle


def draw_fibonacci(n: int) -> None:
    f1: int = 1
    f2: int = 1
    turtle.right(90)
    for i in range(0, n):
        turtle.forward(f1)
        turtle.left(90)
        f3 = f1 + f2
        f1 = f2
        f2 = f3


draw_fibonacci(15)
turtle.done()
