def fast_exp(a: int, n: int) -> int:
    w = 1
    while n > 0:
        if n % 2 == 1:
            w *= a

        a *= a
        n = n // 2

    return w


print(f'2^10 = {fast_exp(2, 10)}')
