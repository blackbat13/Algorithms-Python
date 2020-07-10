nominały = [200, 100, 50, 20, 10, 5, 2, 1]


def reszta_zachłannie(kwota):
    wynik = 0
    i = 0
    while kwota > 0:
        wynik += int(kwota / nominały[i])
        kwota %= nominały[i]
        i += 1

    return wynik


def reszta_dynamicznie(kwota):
    wynik_częściowy = []
    wykorzystane_nominały = []
    nieskonczoność = 10000000

    for i in range(0, kwota + 1):
        wynik_częściowy.append(nieskonczoność)
        wykorzystane_nominały.append(nieskonczoność)

    wynik_częściowy[0] = 0

    ilość_nominałów = int(input('Podaj ilość nominałów: '))

    for j in range(0, ilość_nominałów):
        coin_value = int(input('Podaj wartość kolejnego nominału: '))
        for i in range(0, kwota - coin_value + 1):
            if wynik_częściowy[i] + 1 < wynik_częściowy[i + coin_value]:
                wynik_częściowy[i + coin_value] = wynik_częściowy[i] + 1
                wykorzystane_nominały[i + coin_value] = coin_value

    if wynik_częściowy[kwota] == nieskonczoność:
        print('Nie można wydać kwoty przy użyciu podanych nominałów')
        return

    print(f'Kwota {kwota} może zostać wydana przy użyciu {wynik_częściowy[kwota]} nominałów')
    print('Wykorzystane nominały:')
    i = kwota
    while i > 0:
        print(wykorzystane_nominały[i])
        i -= wykorzystane_nominały[i]


amount = int(input('Podaj kwotę: '))
print('Algorytm zachłanny')
print(f'Kwota {amount} może zostać wydana przy użyciu {reszta_zachłannie(amount)} nominałów')
print('Algorytm dynamiczny')
reszta_dynamicznie(amount)
