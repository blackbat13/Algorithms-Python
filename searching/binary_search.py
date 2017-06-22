def binary_search_iterative(array, number):
    left = 0
    right = len(array) - 1
    while left < right:
        middle = int((left + right) / 2)
        if number < array[middle]:
            right = middle
        elif number > array[middle]:
            left = middle + 1
        else:
            return middle

    if left < len(array) and array[left] == number:
        return left

    return -1


def binary_search_recursive(array, number, left, right):
    if left < right:
        middle = int((left + right) / 2)
        if number < array[middle]:
            return binary_search_recursive(array, number, left, middle)
        elif number > array[middle]:
            return binary_search_recursive(array, number, middle + 1, right)
        else:
            return middle
    elif left < len(array) and array[left] == number:
        return left

    return -1


array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
number = int(input('Enter number to find'))
index1 = binary_search_iterative(array, number)
index2 = binary_search_recursive(array, number, 0, len(array))
if index1 != index2:
    print('Method mismatch')
elif index1 != -1:
    print(f'Index of given number is {index1}')
else:
    print('Number not found')
