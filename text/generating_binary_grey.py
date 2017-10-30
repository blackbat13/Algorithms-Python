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


def generate_grey(n):
    if n == 0:
        return [""]

    previous_result = generate_grey(n - 1)
    new_result = []
    for grey_number in previous_result:
        new_result.append("0" + grey_number)

    previous_result.reverse()
    for grey_number in previous_result:
        new_result.append("1" + grey_number)

    return new_result


number_of_bits = int(input('Enter number of bits: '))

grey_numbers = generate_grey(number_of_bits)
binary_numbers = generate_binary(number_of_bits)

print('binary = grey = decimal')
for number in range(0, len(binary_numbers)):
    print(f'{binary_numbers[number]} = {grey_numbers[number]} = {number}')
