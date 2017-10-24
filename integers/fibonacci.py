def fibonacci_iterative(n):
    if n <= 2:
        return 1

    f1 = 1
    f2 = 1
    for i in range(3, n + 1):
        f3 = f1 + f2
        f1 = f2
        f2 = f3

    return f2


def fibonacci_recursive(n):
    if n <= 2:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


n = int(input('Enter number to compute'))
print(f'Iterative: {fibonacci_iterative(n)}')
print(f'Recursive: {fibonacci_recursive(n)}')
