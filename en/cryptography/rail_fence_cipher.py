def encode(message: str, key: int):
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
