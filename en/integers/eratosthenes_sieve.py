def sieve(n: int) -> list:
    prime = [False, False]
    for i in range(2, n + 1):
        prime.append(True)

    for i in range(2, n):
        if not prime[i]:
            continue

        for j in range(2 * i, n + 1, i):
            prime[j] = False

    return prime


def print_prime_numbers(prime: list) -> None:
    for i in range(0, len(prime)):
        if prime[i]:
            print(i)


n = int(input('Enter number: '))
prime = sieve(n)
print_prime_numbers(prime)
