def rozłóż_na_czynniki_pierwsze(n):
    czynniki_pierwsze = []
    i = 2
    while n > 1:
        if n % i == 0:
            czynniki_pierwsze.append(i)
            n /= i
        else:
            i += 1

    return czynniki_pierwsze


n = int(input('Podaj liczbę: '))
print(f'Czynniki pierwsze liczby {n}: {rozłóż_na_czynniki_pierwsze(n)}')
