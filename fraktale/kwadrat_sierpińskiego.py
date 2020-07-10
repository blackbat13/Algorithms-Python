import turtle as żółw


def kwadrat_sierpińskiego(stopień, długość):
    if stopień == 0:
        żółw.begin_fill()
        for _ in range(0, 4):
            żółw.forward(długość)
            żółw.left(90)
        żółw.end_fill()
        return

    for _ in range(0, 4):
        for _ in range(0, 2):
            żółw.forward(długość / 3)
            kwadrat_sierpińskiego(stopień - 1, długość / 3)
        żółw.forward(długość / 3)
        żółw.left(90)


żółw.color('blue')
żółw.speed(0)
żółw.penup()
żółw.back(200)
żółw.pendown()
kwadrat_sierpińskiego(2, 300)
żółw.done()
