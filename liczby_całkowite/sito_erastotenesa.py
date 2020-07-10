def sito(n):
    pierwsze = [False, False]
    for i in range(2, n + 1):
        pierwsze.append(True)

    for i in range(2, n):
        if not pierwsze[i]:
            continue

        for j in range(2 * i, n + 1, i):
            pierwsze[j] = False

    return pierwsze


def wypisz_liczby_pierwsze(pierwsze):
    for i in range(0, len(pierwsze)):
        if pierwsze[i]:
            print(i)


n = int(input('Enter number: '))
pierwsze = sito(n)
wypisz_liczby_pierwsze(pierwsze)
