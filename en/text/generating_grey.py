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
number = 0
for grey_number in grey_numbers:
    print(f'{grey_number} = {number}')
    number += 1