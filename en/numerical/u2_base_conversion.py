def u2_to_ten(number: str) -> int:
    power = 2 ** (len(number) - 1)
    result = 0
    if number[0] == "1":
        result -= power
    for index in range(1, len(number)):
        power //= 2
        digit = number[index]
        if digit == "1":
            result += power

    return result


print(f"10000001_u2 in ten: {u2_to_ten('10000001')}")
