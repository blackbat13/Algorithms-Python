import math


def is_prime(n: int) -> bool:
    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


n = int(input('Enter number: '))
if is_prime(n):
    print(f'{n} is a prime number')
else:
    print(f'{n} is not a prime number')
