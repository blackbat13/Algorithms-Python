def gcd_iterative(a, b):
    while b != 0:
        b2 = b
        b = a % b
        a = b2

    return a


def gcd_recursive(a, b):
    if b == 0:
        return a
    return gcd_recursive(b, a % b)


def subtraction_gcd(a, b):
    while a > 0 and b > 0:
        if a > b:
            a -= b
        else:
            b -= a

    if a == 0:
        return b
    else:
        return a


a = int(input('Enter a'))
b = int(input('Enter b'))

print(f'Iterative GCD({a},{b}) = {gcd_iterative(a, b)}')
print(f'Recursive GCD({a},{b}) = {gcd_recursive(a, b)}')
print(f'Subtraction GCD({a},{b}) = {subtraction_gcd(a, b)}')
