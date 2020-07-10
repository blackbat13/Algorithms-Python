def encode(message: str, key: int) -> str:
    """
        Encodes message using Rail Fence Cipher with given key
        :param message: message to encode
        :param key: key
        :return: message encode using Rail Fence with given key
        """
    encoded: str = ''
    k: int = 0
    jump: int = 0
    for k in range(key):
        if k == key - 1:
            jump = (key - 1) * 2
        else:
            jump = (key - (k + 1)) * 2
        i = k
        while i < len(message):
            encoded += message[i]
            i += jump

    return encoded


def decode(message: str, key: int) -> str:
    """
        Decodes message using Rail Fence Cipher with given key
        :param message: message to encode
        :param key: key
        :return: message decoded using Rail Fence Cipher with given key
    """
    decoded: list = list(message)
    j: int = 0
    jump: int = 0
    for k in range(key):
        if k == key - 1:
            jump = (key - 1) * 2
        else:
            jump = (key - (k + 1)) * 2
        i = k
        while i < len(message):
            decoded[i] = message[j]
            j += 1
            i += jump

    return ''.join(decoded)


message: str = 'computer science'
encoded: str = encode(message, 3)
decoded: str = decode(encoded, 3)
print(f'Encoded: {encoded}')
print(f'Decoded: {decoded}')
