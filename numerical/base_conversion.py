def from_ten(number, new_base):
    converted = ""
    while number > 0:
        rest = number % new_base
        number -= rest
        number = int(number / new_base)
        if rest > 9:
            converted = chr(ord('A') + rest - 10) + converted
        else:
            converted = str(rest) + converted

    return converted


def to_ten(number, base):
    converted = 0
    power = 1
    i = len(number) - 1
    while i >= 0:
        if ord(number[i]) <= ord('9'):
            converted += int(number[i]) * power
        else:
            value = ord(number[i]) - ord('A') + 10
            converted += value * power
        power *= base
        i -= 1

    return converted


number = 241
base = 16
converted = from_ten(number, base)
print(f'{number} in {base} is {converted}')
print(f'{converted} in 10 is {to_ten(converted, base)}')
