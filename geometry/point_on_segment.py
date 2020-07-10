def point_on_segment(a_x: int, a_y: int, b_x: int, b_y: int, c_x: int, c_y: int) -> bool:
    """
        Check if point (c_x, c_y) lies on the segment [(a_x, a_y), (b_x, b_y)]
    :return: True if point lies on the given segment, False otherwise
    """
    # matrix = [
    #     [a_x, a_y, 1],
    #     [b_x, b_y, 1],
    #     [c_x, c_y, 1]]
    det: int = a_x * b_y * 1 + b_x * c_y * 1 + c_x * a_y * 1 - b_x * a_y * 1 - a_x * c_y * 1 - c_x * b_y * 1
    if det != 0:
        return False

    if min(a_x, b_x) <= c_x <= max(a_x, b_x) and min(a_y, b_y) <= c_y <= max(a_y, b_y):
        return True
    else:
        return False


print(point_on_segment(1, 1, 5, 5, 2, 2))
