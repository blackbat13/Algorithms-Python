def is_palindrome(a: str) -> bool:
    return a == ''.join(reversed(a))


a: str = input('Enter string: ')
if is_palindrome(a):
    print(f'{a} is a palindrome')
else:
    print(f'{a} is not a palindrome')
