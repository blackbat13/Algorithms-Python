def is_palindrome(a):
    b = ''.join(reversed(a))
    return a == b


a = input('Enter string: ')
if is_palindrome(a):
    print(f'{a} is a palindrome')
else:
    print(f'{a} is not a palindrome')
