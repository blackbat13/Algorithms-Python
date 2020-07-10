def are_anagrams(a: str, b: str) -> bool:
    return sorted(a) == sorted(b)


a: str = input('Enter first string: ')
b: str = input('Enter second string: ')
if are_anagrams(a, b):
    print(f'{a} and {b} are anagrams')
else:
    print(f'{a} and {b} are not anagrams')
