def is_letter(letter: str):
    return ord('a') <= ord(letter) <= ord('z')


def encode(message: str, key: str):
    encoded = ''
    key_index = 0
    for i in range(0, len(message)):
        if not is_letter(message[i]):
            encoded += message[i]
            continue
        k = ord(key[key_index]) - ord('a')
        letter = ord(message[i]) + k
        if letter > ord('z'):
            letter = ord('a') + letter - ord('z')

        letter = chr(letter)
        encoded += letter
        key_index += 1
        key_index %= len(key)

    return encoded


def decode(message: str, key: str):
    decoded = ''
    key_index = 0
    for i in range(0, len(message)):
        if not is_letter(message[i]):
            decoded += message[i]
            continue
        k = ord(key[key_index]) - ord('a')
        letter = ord(message[i]) - k
        if letter < ord('a'):
            letter = ord('z') - (ord('a') - letter)

        letter = chr(letter)
        decoded += letter
        key_index += 1
        key_index %= len(key)

    return decoded


message = 'computer science'
encoded = encode(message, 'cat')
decoded = decode(encoded, 'cat')
print(f'Encoded: {encoded}')
print(f'Decoded: {decoded}')
