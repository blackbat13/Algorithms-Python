def is_letter(letter: str) -> bool:
    return ord('a') <= ord(letter) <= ord('z')


def encode(message: str, key: str) -> str:
    encoded: str = ''
    key_index: int = 0
    letter: int = 0
    k: int = 0
    for i in range(len(message)):
        if not is_letter(message[i]):
            encoded += message[i]
            continue
        k = ord(key[key_index]) - ord('a')
        letter = ord(message[i]) + k
        if letter > ord('z'):
            letter = ord('a') + letter - ord('z')

        encoded += chr(letter)
        key_index += 1
        key_index %= len(key)

    return encoded


def decode(message: str, key: str) -> str:
    decoded: str = ''
    key_index: int = 0
    letter: int = 0
    k: int = 0
    for i in range(len(message)):
        if not is_letter(message[i]):
            decoded += message[i]
            continue
        k = ord(key[key_index]) - ord('a')
        letter = ord(message[i]) - k
        if letter < ord('a'):
            letter = ord('z') - (ord('a') - letter)

        decoded += chr(letter)
        key_index += 1
        key_index %= len(key)

    return decoded


message: str = 'computer science'
encoded: str = encode(message, 'cat')
decoded: str = decode(encoded, 'cat')
print(f'Encoded: {encoded}')
print(f'Decoded: {decoded}')
