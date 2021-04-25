def linear_search(array: list, number: int) -> int:
    for i in range(len(array)):
        if number == array[i]:
            return i

    return -1


array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
number = int(input('Enter number to find: '))
index = linear_search(array, number)
if index == -1:
    print('Number not found')
else:
    print(f'Number position is {index}')
