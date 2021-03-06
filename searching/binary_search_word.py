def fill_letters(letters: list) -> None:
    for i in range(ord('a'), ord('z') + 1):
        letters.append(chr(i))


def find_letter() -> str:
    first: int = ord('a')
    last: int = ord('z')
    while first != last:
        mid = (first + last) // 2
        answer = input(f'Is this letter located in the alphabet after {chr(mid)}?')
        if answer == 'y':
            first = mid + 1
        elif answer == 'n':
            last = mid
        else:
            print('Please answer using only single letter y or n.')

    return chr(first)


print('First think about a single word. Then I will ask you a few questions to find that word.')
print('Below is the alphabet to help you answering questions.')
print('Please answer all the questions (excluding the first one) using one letter: y (for yes) or n (for no).')

letters: list = []
fill_letters(letters)
print()
print(letters)

length: int = int(input('What is the length of the word?'))
word: str = ''
for i in range(length):
    print(f'Now I will ask you about letter {i+1}')
    word += find_letter()
    print('Ok, i got it!')
    print()

print(f'You were thinking about {word}!')
