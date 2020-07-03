def grey_to_binary(grey: str) -> str:
    binary: str = grey[0]
    number: int = 0
    for i in range(1, len(grey)):
        number = int(binary[i - 1])
        number += int(grey[i])
        number %= 2
        binary += str(number)

    return binary


grey = "101"
print(f'{grey} = {grey_to_binary(grey)}')
