import random


def monte_carlo_pi(points_count: int) -> float:
    num_points_in_circle: int = 0
    center_x: int = 1
    center_y: int = 1
    radius: int = 1
    x: float = 0
    y: float = 0
    distance: float = 0
    for _ in range(points_count):
        x = random.random() * 2.0
        y = random.random() * 2.0
        distance = ((x - center_x) ** 2) + ((y - center_y) ** 2)
        if distance <= radius ** 2:
            num_points_in_circle += 1

    return (4 * num_points_in_circle) / points_count


points_count: int = int(input('Number of points: '))
print(f'Estimated value of PI is: {monte_carlo_pi(points_count)}')
