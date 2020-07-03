def can_create_triangle(a: int, b: int, c: int) -> bool:
    return a < b + c and b < a + c and c < a + b


a: int = 3
b: int = 8
c: int = 9

if can_create_triangle(a, b, c):
    print(f'Triangle can be created from {a}, {b} and {c}')
else:
    print(f'Triangle cannot be created from {a}, {b} and {c}')
