def generate_binary(n):
    if n == 0:
        return [""]

    previous_result = generate_binary(n - 1)
    new_result = []
    for binary_number in previous_result:
        new_result.append("0" + binary_number)
    for binary_number in previous_result:
        new_result.append("1" + binary_number)

    return new_result


number_of_bits = int(input('Enter number of bits: '))
binary_numbers = generate_binary(number_of_bits)
number = 0
for binary_number in binary_numbers:
    print(f'{binary_number} = {number}')
    number += 1
