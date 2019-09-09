def is_letter(letter):
    return ord('a') <= ord(letter) <= ord('z')


def encode(message:str):
    encoded = ''
    k = 0
    for i in range(0, len(message)):
        if not is_letter(message[i]):
            encoded += message[i]
            continue
        letter = ord(message[i]) + k
        if letter > ord('z'):
            letter = ord('a') + letter - ord('z')

        letter = chr(letter)
        encoded += letter
        k += 1
        k %= 26

    return encoded


def decode(message:str):
    decoded = ''
    k = 0
    for i in range(0, len(message)):
        if not is_letter(message[i]):
            decoded += message[i]
            continue
        letter = ord(message[i]) - k
        if letter < ord('a'):
            letter = ord('z') - (ord('a') - letter)

        letter = chr(letter)
        decoded += letter
        k += 1
        k %= 26

    return decoded


message = 'computer science'
encoded = encode(message)
decoded = decode(encoded)
print(f'Encoded: {encoded}')
print(f'Decoded: {decoded}')
