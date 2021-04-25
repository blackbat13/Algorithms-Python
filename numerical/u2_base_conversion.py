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


number_u2 = "10000001"
number_ten = u2_to_ten(number_u2)
print(f"{number_u2} (U2) = {number_ten} (10)")
