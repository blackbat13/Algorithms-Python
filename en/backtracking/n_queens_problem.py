def find_solution(n: int, queen_id: int, positions: list):
    if queen_id == n:
        return True

    for i in range(0, n):
        if not check_new_position(queen_id, i, positions):
            continue

        positions[queen_id] = i
        result = find_solution(n, queen_id + 1, positions)
        if result:
            return True

    return False


def check_new_position(x: int, y: int, positions: list):
    for i in range(0, x):
        if positions[i] == y:
            return False
        if y - positions[i] == x - i:
            return False

    return True


n = 5
positions = [0 for _ in range(n)]
result = find_solution(n, 0, positions)
if result:
    print(positions)
