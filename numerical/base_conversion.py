def from_ten(number: int, new_base: int) -> str:
    converted: str = ""
    rest: int = 0
    while number > 0:
        rest = number % new_base
        number -= rest
        number = int(number / new_base)
        if rest > 9:
            converted = chr(ord('A') + rest - 10) + converted
        else:
            converted = str(rest) + converted

    return converted


def to_ten(number: str, base: int) -> int:
    converted: int = 0
    power: int = 1
    i: int = len(number) - 1
    while i >= 0:
        if ord(number[i]) <= ord('9'):
            converted += int(number[i]) * power
        else:
            value = ord(number[i]) - ord('A') + 10
            converted += value * power
        power *= base
        i -= 1

    return converted


number: int = 241
base: int = 16
converted: str = from_ten(number, base)
print(f'{number} in {base} is {converted}')
print(f'{converted} in 10 is {to_ten(converted, base)}')
