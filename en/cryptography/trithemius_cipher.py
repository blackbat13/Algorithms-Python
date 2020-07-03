def is_letter(letter: str) -> bool:
    return ord('a') <= ord(letter) <= ord('z')


def encode(message: str) -> bool:
    encoded: str = ''
    k: int = 0
    letter: int = 0
    for i in range(len(message)):
        if not is_letter(message[i]):
            encoded += message[i]
            continue
        letter = ord(message[i]) + k
        if letter > ord('z'):
            letter = ord('a') + letter - ord('z')

        encoded += chr(letter)
        k += 1
        k %= 26

    return encoded


def decode(message: str) -> str:
    decoded: str = ''
    k: int = 0
    letter: int = 0
    for i in range(len(message)):
        if not is_letter(message[i]):
            decoded += message[i]
            continue
        letter = ord(message[i]) - k
        if letter < ord('a'):
            letter = ord('z') - (ord('a') - letter)

        decoded += chr(letter)
        k += 1
        k %= 26

    return decoded


message: str = 'computer science'
encoded: str = encode(message)
decoded: str = decode(encoded)
print(f'Encoded: {encoded}')
print(f'Decoded: {decoded}')
