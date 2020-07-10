def nwd_iteracyjnie(a, b):
    while b != 0:
        b2 = b
        b = a % b
        a = b2

    return a


def nwd_rekurencyjnie(a, b):
    if b == 0:
        return a
    return nwd_rekurencyjnie(b, a % b)


def nwd_z_odejmowaniem(a, b):
    while a > 0 and b > 0:
        if a > b:
            a -= b
        else:
            b -= a

    if a == 0:
        return b
    else:
        return a


a = int(input('Podaj a: '))
b = int(input('Podaj b: '))

print(f'Iteracyjnie NWD({a},{b}) = {nwd_iteracyjnie(a, b)}')
print(f'Rekurencyjnie NWD({a},{b}) = {nwd_rekurencyjnie(a, b)}')
print(f'Z odejmowaniem NWD({a},{b}) = {nwd_z_odejmowaniem(a, b)}')
