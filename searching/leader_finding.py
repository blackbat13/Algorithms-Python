def find_leader(array: list) -> int:
    counter: int = 0
    current_candidate: int = 0
    for el in array:
        if counter == 0:
            current_candidate = el
            counter = 1
        else:
            if el == current_candidate:
                counter += 1
            else:
                counter -= 1

    return current_candidate


def count_occurrences(element: int, array: list) -> int:
    count: int = 0
    for el in array:
        if el == element:
            count += 1

    return count


array: list = [1, 2, 5, 5, 7, 5, 5, 10, 5, 5]
majority: int = find_leader(array)
if count_occurrences(majority, array) >= len(array) / 2:
    print(f'Majority element is: {majority}')
else:
    print('There is no majority element in given list')
