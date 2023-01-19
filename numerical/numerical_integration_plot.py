import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches


def f(x: float) -> float:
    return np.sin(x)


def rectangles_method(a: int, b: int, n: int) -> float:
    rectangle_width = (b - a) / n
    area = 0
    current_point = a

    for i in range(n):
        current_point += rectangle_width
        rectangle_height = f(current_point)
        area += rectangle_height * rectangle_width
        rect = mpatches.Rectangle((current_point - rectangle_width, 0), rectangle_width,
                                  rectangle_height, fill=False, color="purple", linewidth=2)
        plt.gca().add_patch(rect)

    return area


def trapezes_method(a: int, b: int, n: int) -> float:
    trapeze_height = (b - a) / n
    area = 0
    current_point = a

    for i in range(n):
        trapeze_first_side = f(current_point)
        current_point += trapeze_height
        trapeze_second_side = f(current_point)
        area += ((trapeze_first_side + trapeze_second_side)
                 * trapeze_height) / 2

        pol = mpatches.Polygon(xy=[(current_point - trapeze_height, 0),
                                   (current_point - trapeze_height,
                                    trapeze_first_side),
                                   (current_point, trapeze_second_side),
                                   (current_point, 0)], fill=False, color="red", linewidth=2)
        plt.gca().add_patch(pol)

    return area


def draw_plot(a, b, n):
    x = np.linspace(-max(abs(a), abs(b)), max(abs(a), abs(b)), n * 10)
    y = np.sin(x)

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    plt.plot(x, y, 'b', label='f(x)=sin(x)')
    plt.legend()


draw_plot(-4, 4, 100)

print(f'Rectangles method result: {rectangles_method(0, 3, 10)}')
print(f'Trapezes method result: {trapezes_method(-3, 0, 10)}')

plt.show()
