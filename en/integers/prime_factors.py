from typing import List


def distribute(n: int) -> List[int]:
    prime_factors: List[int] = []
    i: int = 2
    while n > 1:
        if n % i == 0:
            prime_factors.append(i)
            n /= i
        else:
            i += 1

    return prime_factors


n: int = int(input('Enter number: '))
print(f'Prime factors of {n}: {distribute(n)}')
