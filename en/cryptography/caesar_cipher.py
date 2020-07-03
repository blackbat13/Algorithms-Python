def is_letter(character: str) -> bool:
    """
    Checks if given character is a (small) letter
    :param character: character to check
    :return: True if character is a (small) letter, False otherwise
    """
    return ord('a') <= ord(character) <= ord('z')


def encode(message: str, key: int) -> str:
    """
    Encodes message using Caesar Cipher with given key
    :param message: message to encode
    :param key: key
    :return: message encoded using Caesar Cipher with given key
    """
    encoded: str = ''
    letter: int = 0
    for i in range(len(message)):
        if not is_letter(message[i]):
            encoded += message[i]
            continue
        letter = ord(message[i]) + key
        if letter > ord('z'):
            letter = ord('a') + letter - ord('z')

        encoded += chr(letter)

    return encoded


def decode(message: str, key: int) -> str:
    """
        Decodes message using Caesar Cipher with given key
        :param message: message to encode
        :param key: key
        :return: message decoded using Caesar Cipher with given key
    """
    decoded: str = ''
    letter: int = 0
    for i in range(len(message)):
        if not is_letter(message[i]):
            decoded += message[i]
            continue
        letter = ord(message[i]) - key
        if letter < ord('a'):
            letter = ord('z') - (ord('a') - letter)

        decoded += chr(letter)

    return decoded


message: str = 'computer science'
encoded: str = encode(message, 3)
decoded: str = decode(encoded, 3)
print(f'Encoded: {encoded}')
print(f'Decoded: {decoded}')
