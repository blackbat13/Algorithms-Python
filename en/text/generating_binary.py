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


number_of_bits: int = int(input('Enter number of bits: '))
binary_numbers: List[str] = generate_binary(number_of_bits)
number: int = 0
for binary_number in binary_numbers:
    print(f'{binary_number} = {number}')
    number += 1
