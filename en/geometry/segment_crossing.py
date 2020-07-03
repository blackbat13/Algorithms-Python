def point_on_segment(a_x: int, a_y: int, b_x: int, b_y: int, c_x: int, c_y: int) -> bool:
    det: int = a_x * b_y * 1 + b_x * c_y * 1 + c_x * a_y * 1 - b_x * a_y * 1 - a_x * c_y * 1 - c_x * b_y * 1
    if det != 0:
        return False

    if min(a_x, b_x) <= c_x <= max(a_x, b_x) and min(a_y, b_y) <= c_y <= max(a_y, b_y):
        return True
    else:
        return False


def sgn(a: int) -> int:
    if a < 0:
        return -1
    elif a > 0:
        return 1
    else:
        return 0


def det3(matrix: list) -> int:
    return matrix[0][0] * matrix[1][1] * matrix[2][2] + matrix[1][0] * matrix[2][1] * matrix[0][2] + matrix[2][0] * \
           matrix[0][1] * matrix[1][2] - matrix[0][2] * matrix[1][1] * matrix[2][0] - matrix[0][1] * matrix[1][0] * \
           matrix[2][2] - matrix[0][0] * matrix[1][2] * matrix[2][1]


def segment_crossing(a_x: int, a_y: int, b_x: int, b_y: int, c_x: int, c_y: int, d_x: int, d_y: int) -> bool:
    if point_on_segment(a_x, a_y, b_x, b_y, c_x, c_y) or \
            point_on_segment(a_x, a_y, b_x, b_y, d_x, d_y) or \
            point_on_segment(c_x, c_y, d_x, d_y, a_x, a_y) or \
            point_on_segment(c_x, c_y, d_x, d_y, b_x, b_y):
        return True

    if sgn(det3([[a_x, a_y, 1], [b_x, b_y, 1], [c_x, c_y, 1]])) == sgn(
            det3([[a_x, a_y, 1], [b_x, b_y, 1], [d_x, d_y, 1]])):
        return False
    else:
        return True


print(segment_crossing(1, 1, 2, 2, 3, 3, 4, 4))
print(segment_crossing(1, 1, 5, 5, 1, 5, 5, 5))
