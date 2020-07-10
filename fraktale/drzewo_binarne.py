import turtle as żółw


def drzewo_binarne(stopień, długość):
    żółw.forward(długość)
    if stopień > 0:
        żółw.left(45)
        drzewo_binarne(stopień - 1, długość / 2)
        żółw.right(90)
        drzewo_binarne(stopień - 1, długość / 2)
        żółw.left(45)
    żółw.back(długość)


żółw.speed(0)
żółw.penup()
żółw.left(90)
żółw.back(350)
żółw.pendown()
żółw.pensize(3)
drzewo_binarne(5, 400)
żółw.done()
