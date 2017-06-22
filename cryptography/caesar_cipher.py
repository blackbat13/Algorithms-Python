def is_letter(letter):
    return ord('a') <= ord(letter) <= ord('z')


def encode(message, k):
    encoded = ''
    for i in range(0, len(message)):
        if not is_letter(message[i]):
            encoded += message[i]
            continue
        letter = ord(message[i]) + k
        if letter > ord('z'):
            letter = ord('a') + letter - ord('z')

        letter = chr(letter)
        encoded += letter

    return encoded


def decode(message, k):
    decoded = ''
    for i in range(0, len(message)):
        if not is_letter(message[i]):
            decoded += message[i]
            continue
        letter = ord(message[i]) - k
        if letter < ord('a'):
            letter = ord('z') - (ord('a') - letter)

        letter = chr(letter)
        decoded += letter

    return decoded


message = 'computer science'
encoded = encode(message, 3)
decoded = decode(encoded, 3)
print(f'Encoded: {encoded}')
print(f'Decoded: {decoded}')
