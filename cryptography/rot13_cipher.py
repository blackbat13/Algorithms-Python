def is_letter(letter: str) -> bool:
    return ord('a') <= ord(letter) <= ord('z')


def encode(message: str) -> str:
    encoded: str = ''
    letter: int = 0
    for i in range(len(message)):
        if not is_letter(message[i]):
            encoded += message[i]
            continue
        letter = ord(message[i]) + 13
        if letter > ord('z'):
            letter = ord('a') + letter - ord('z')

        encoded += chr(letter)

    return encoded


def decode(message: str) -> str:
    decoded: str = ''
    letter: int = 0
    for i in range(len(message)):
        if not is_letter(message[i]):
            decoded += message[i]
            continue
        letter = ord(message[i]) - 13
        if letter < ord('a'):
            letter = ord('z') - (ord('a') - letter)

        decoded += chr(letter)

    return decoded


message: str = 'computer science'
encoded: str = encode(message)
decoded: str = decode(encoded)
print(f'Encoded: {encoded}')
print(f'Decoded: {decoded}')
