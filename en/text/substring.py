def substring_pos(a, b):
    for i in range(0, len(a) - len(b)):
        j = 0
        while j < len(b) and b[j] == a[i + j]:
            j += 1

        if j == len(b):
            return i

    return -1


a = input('Enter string to search in: ')
b = input('Enter string to search for: ')

pos = substring_pos(a, b)
if pos == -1:
    print(f'{b} is not a substring of {a}')
else:
    print(f'{b} is substring of {a} and starts at position {pos}')
