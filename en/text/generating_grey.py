from typing import List


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
number: int = 0
for grey_number in grey_numbers:
    print(f'{grey_number} = {number}')
    number += 1
