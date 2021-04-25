def are_anagrams(a: str, b: str) -> bool:
    return sorted(a) == sorted(b)


a = input('Enter first string: ')
b = input('Enter second string: ')
if are_anagrams(a, b):
    print(f'{a} and {b} are anagrams')
else:
    print(f'{a} and {b} are not anagrams')
