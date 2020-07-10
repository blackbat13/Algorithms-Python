def jest_doskonała(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i

    return sum == n


n = int(input('Podaj liczbę: '))
if jest_doskonała(n):
    print(f'{n} jest liczbą doskonałą')
else:
    print(f'{n} nie jest liczbą doskonałą')
