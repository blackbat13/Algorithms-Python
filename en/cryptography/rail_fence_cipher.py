def encode(message: str, key: int):
    """
        Encodes message using Rail Fence Cipher with key key
        :param message: message to encode
        :param key: key
        :return: message encode using Rail Fence with key key
        """
    encoded = ''
    for k in range(0, key):
        if k == key - 1:
            jump = (key - 1) * 2
        else:
            jump = (key - (k + 1)) * 2
        i = k
        while i < len(message):
            encoded += message[i]
            i += jump

    return encoded


def decode(message: str, key: int):
    """
        Decodes message using Rail Fence Cipher with key key
        :param message: message to encode
        :param key: key
        :return: message decoded using Rail Fence Cipher with key key
    """
    decoded = list(message)
    j = 0
    for k in range(0, key):
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


message = 'computer science'
encoded = encode(message, 3)
decoded = decode(encoded, 3)
print(f'Encoded: {encoded}')
print(f'Decoded: {decoded}')
