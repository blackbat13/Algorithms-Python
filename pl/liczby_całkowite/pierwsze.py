import math


def jest_pierwsza(n):
    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


n = int(input('Podaj liczbę: '))
if jest_pierwsza(n):
    print(f'{n} jest liczbą pierwszą')
else:
    print(f'{n} nie jest liczbą pierwszą')
