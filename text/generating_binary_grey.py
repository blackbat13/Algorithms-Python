from typing import List


def generate_binary(n: int) -> List[str]:
    if n == 0:
        return [""]

    previous_result: List[str] = generate_binary(n - 1)
    new_result: List[str] = []
    for binary_number in previous_result:
        new_result.append("0" + binary_number)
    for binary_number in previous_result:
        new_result.append("1" + binary_number)

    return new_result


def generate_grey(n: int) -> List[str]:
    if n == 0:
        return [""]

    previous_result: List[str] = generate_grey(n - 1)
    new_result: List[str] = []
    for grey_number in previous_result:
        new_result.append("0" + grey_number)

    previous_result.reverse()
    for grey_number in previous_result:
        new_result.append("1" + grey_number)

    return new_result


number_of_bits: int = int(input('Enter number of bits: '))
grey_numbers: List[str] = generate_grey(number_of_bits)
binary_numbers: List[str] = generate_binary(number_of_bits)
print('binary = grey = decimal')
for number in range(0, len(binary_numbers)):
    print(f'{binary_numbers[number]} = {grey_numbers[number]} = {number}')
