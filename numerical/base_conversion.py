def from_ten(number: int, new_base: int) -> str:
    converted = ""
    remainder = 0
    while number > 0:
        remainder = number % new_base
        number -= remainder
        number = int(number / new_base)
        if remainder > 9:
            converted = chr(ord('A') + remainder - 10) + converted
        else:
            converted = str(remainder) + converted

    return converted


def to_ten(number: str, base: int) -> int:
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
print(f'{number} (10) = {converted} ({base})')
print(f'{converted} ({base}) = {to_ten(converted, base)} (10)')
