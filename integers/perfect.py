def is_perfect(n: int) -> bool:
    sum: int = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i

    return sum == n


n: int = int(input('Enter number: '))
if is_perfect(n):
    print(f'{n} is a perfect number')
else:
    print(f'{n} is not a perfect number')
