import math


def wypełnij_litery():
    for i in range(ord('a'), ord('z') + 1):
        litery.append(chr(i))


def znajdź_literę():
    pierwsza = ord('a')
    ostatnia = ord('z')
    while pierwsza != ostatnia:
        mid = math.floor((pierwsza + ostatnia) / 2)
        answer = input(f'Czy ta litera znajduje się w alfabecie po literze {chr(mid)}?')
        if answer == 't':
            pierwsza = mid + 1
        elif answer == 'n':
            ostatnia = mid
        else:
            print('Odpowiadaj proszę używając jedynie pojedyńczych liter t lub n.')

    return chr(pierwsza)


print('Najpierw pomyśl o jednym wyrazie. Następnie zadam Ci kilka pytań, aby odkryć ten wyraz.')
print('Poniżej znajdziesz alfabet, który pomoże Ci w odpowiadaniu na pytania.')
print('Używaj wyłącznie liter z podanego alfabetu angielskiego. Nie używaj polskich znaków.')
print('Na wszystkie pytania (poza pierwszym) odpowiadaj używając jednej litery: t (tak) lub n (nie).')

litery = []
wypełnij_litery()
print()
print(litery)

długość = int(input('Z ilu liter składa się Twój wyraz?'))
wyraz = ''
for i in range(0, długość):
    print(f'Teraz zadam Ci kilka pytań o literę o numerze {i+1}')
    wyraz += znajdź_literę()
    print('Już wiem!')
    print()

print(f'Pomyślany przez Ciebie wyraz to {wyraz}!')
