def is_letter(letter):
    return ord('a') <= ord(letter) <= ord('z')


def encode(message:str, key:str):
    encoded = ''
    key_index = 0
    for i in range(0, len(message)):
        if not is_letter(message[i]):
            encoded += message[i]
            continue
        k = 26 - (ord(message[i]) - ord('a')) + (ord(key[key_index]) - ord('a'))
        k %= 26
        letter = ord('a') + k
        if letter > ord('z'):
            letter = ord('a') + letter - ord('z')

        letter = chr(letter)
        encoded += letter
        key_index += 1
        key_index %= len(key)

    return encoded


message = 'computer science'
encoded = encode(message, 'cat')
decoded = encode(encoded, 'cat')
print(f'Encoded: {encoded}')
print(f'Decoded: {decoded}')
