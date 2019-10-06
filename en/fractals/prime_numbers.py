import turtle


def sieve(n: int):
    prime = [False, False]
    result = []
    for i in range(2, n + 1):
        prime.append(True)

    for i in range(2, n):
        if not prime[i]:
            continue

        result.append(i)
        for j in range(2 * i, n + 1, i):
            prime[j] = False

    return result


def draw_prime(n: int):
    prime_numbers = sieve(n)

    for prime in prime_numbers:
        turtle.forward(prime)
        turtle.left(90)


draw_prime(1000)
turtle.done()
