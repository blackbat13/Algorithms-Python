def f(x):
    return x * x + 2 * x


def rectangles_method(a, b, n):
    rectangle_width = (b - a) / n
    area = 0
    current_point = a

    for i in range(0, n):
        current_point += rectangle_width
        rectangle_height = f(current_point)
        area += rectangle_height * rectangle_width

    return area


def trapezes_method(a, b, n):
    trapeze_height = (b - a) / n
    area = 0
    current_point = a

    for i in range(0, n):
        trapeze_first_side = f(current_point)
        current_point += trapeze_height
        trapeze_second_side = f(current_point)

        area += ((trapeze_first_side + trapeze_second_side) * trapeze_height) / 2

    return area


a = 0
b = 10
n = 100
print(f'Rectangles method result: {rectangles_method(a, b, n)}')
print(f'Trapezes method result: {trapezes_method(a, b, n)}')
