import matplotlib.pyplot as plt


def sqrt(n: float, p: float) -> float:
    x1 = n / 2
    x2 = (x1 + (n / x1)) / 2
    plot_values = [x1, x2]
    while abs(x2 - x1) > p:
        x1 = (x2 + n / x2) / 2
        x1, x2 = x2, x1
        plot_values.append(x2)

    plt.plot(plot_values, label=f"heron({n},{p})")
    plt.legend()

    return x2


n = 9.0
p = 0.00000001

result = sqrt(n, p)

print(f"sqrt({n}) ~= {result}")

plt.show()
