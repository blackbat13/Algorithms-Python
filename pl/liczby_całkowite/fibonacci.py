def fibonacci_iteracyjny(n):
    if n <= 2:
        return 1

    f1 = 1
    f2 = 1
    for i in range(3, n + 1):
        f3 = f1 + f2
        f1 = f2
        f2 = f3

    return f2


def fibonacci_rekurencyjny(n):
    if n <= 2:
        return 1
    return fibonacci_rekurencyjny(n - 1) + fibonacci_rekurencyjny(n - 2)


n = int(input('Podaj liczbę: '))
print(f'Iteracyjnie: {fibonacci_iteracyjny(n)}')
print(f'Rekurencyjnie: {fibonacci_rekurencyjny(n)}')
