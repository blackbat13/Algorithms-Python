import math


def sqrt(n, p):
    x1 = n / 2
    x2 = (x1 + n / x1) / 2
    while math.fabs(x2 - x1) > p:
        x1 = (x2 + n / x2) / 2
        tmp = x1
        x1 = x2
        x2 = tmp

    return x2


print(f'sqrt(9) = {sqrt(9, 0.00000001)}')
