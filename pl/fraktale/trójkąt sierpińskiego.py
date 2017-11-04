import turtle as żółw


def trójkąt_sierpińskiego(stopień, długość):
    if stopień == 0:
        żółw.begin_fill()
        for _ in range(0, 3):
            żółw.forward(długość)
            żółw.left(120)
        żółw.end_fill()
        return

    for _ in range(0, 3):
        trójkąt_sierpińskiego(stopień - 1, długość / 2)
        żółw.forward(długość)
        żółw.left(120)


żółw.speed(0)
żółw.penup()
żółw.back(200)
żółw.pendown()
trójkąt_sierpińskiego(4, 300)
żółw.done()
