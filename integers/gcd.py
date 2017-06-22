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


a = int(input('Enter a'))
b = int(input('Enter b'))

print(f'Iterative GCD({a},{b}) = {gcd_iterative(a, b)}')
print(f'Recursive GCD({a},{b}) = {gcd_recursive(a, b)}')
