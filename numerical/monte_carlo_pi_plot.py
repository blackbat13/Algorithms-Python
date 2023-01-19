import random

import matplotlib.pyplot as plt


def monte_carlo_pi(points_count: int) -> float:
    """Computes the estimated value of PI using a Monte Carlo method.

    Args:
        points_count (int): number of points to draw 

    Returns:
        float: the estimated value of PI, using a Monte Carlo approach.
    """
    num_points_in_circle = 0
    center_x = 1
    center_y = 1
    radius = 1
    x = 0
    y = 0
    distance = 0
    plot_values = []

    for i in range(1, points_count + 1):
        x = random.random() * 2.0
        y = random.random() * 2.0
        distance = ((x - center_x) ** 2) + ((y - center_y) ** 2)

        if distance <= radius ** 2:
            num_points_in_circle += 1

        plot_values.append((4 * num_points_in_circle) / i)

    plt.plot(plot_values)
    plt.xlabel("Number of points")
    plt.ylabel("Estimated PI value")
    plt.title("Monte Carlo method for computing PI value")

    return (4 * num_points_in_circle) / points_count


points_count = 1000

estimated_pi = monte_carlo_pi(points_count)

print(f"PI ~= {estimated_pi}")

plt.show()
