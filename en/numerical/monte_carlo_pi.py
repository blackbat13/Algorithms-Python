import random


def monte_carlo_pi(no_points):
    no_points_in_circle = 0
    center_x = 1
    center_y = 1
    radius = 1
    for _ in range(0, no_points):
        x = random.random() * 2.0
        y = random.random() * 2.0
        distance = ((x - center_x) ** 2) + ((y - center_y) ** 2)
        if distance <= radius ** 2:
            no_points_in_circle += 1

    return (4 * no_points_in_circle) / no_points


no_points = int(input('Number of points: '))
print(f'Estimated value of PI is: {monte_carlo_pi(no_points)}')
