def distribute(n):
    prime_factors = []
    i = 2
    while n > 1:
        if n % i == 0:
            prime_factors.append(i)
            n /= i
        else:
            i += 1

    return prime_factors


n = int(input('Enter number'))
print(f'Prime factors of {n}: {distribute(n)}')
