def is_letter(character: str):
    """
    Checks if given character is a (small) letter
    :param character: character to check
    :return: True if character is a (small) letter, False otherwise
    """
    return ord('a') <= ord(character) <= ord('z')


def encode(message: str, k: int):
    """
    Encodes message using Caesar Cipher with key k
    :param message: message to encode
    :param k: key
    :return: message encoded using Caesar Cipher with key k
    """
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


def decode(message: str, k: int):
    """
        Decodes message using Caesar Cipher with key k
        :param message: message to encode
        :param k: key
        :return: message decoded using Caesar Cipher with key k
    """
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
