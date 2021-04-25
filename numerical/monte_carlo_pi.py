import random


def monte_carlo_pi(points_count: int) -> float:
    num_points_in_circle = 0
    center_x = 1
    center_y = 1
    radius = 1
    x = 0
    y = 0
    distance = 0
    for _ in range(points_count):
        x = random.random() * 2.0
        y = random.random() * 2.0
        distance = ((x - center_x) ** 2) + ((y - center_y) ** 2)
        if distance <= radius ** 2:
            num_points_in_circle += 1

    return (4 * num_points_in_circle) / points_count


points_count = int(input('Number of points: '))
estimated_pi = monte_carlo_pi(points_count)
print(f'Estimated value of PI is: {estimated_pi}')
