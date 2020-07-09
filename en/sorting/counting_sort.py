from typing import List


def counting_sort(array: List[int]):
    result: List[int] = []
    max_number: int = 100
    occurrences: List[int] = [0 for _ in range(max_number + 1)]

    for number in array:
        occurrences[number] += 1

    for i in range(len(occurrences)):
        for j in range(occurrences[i]):
            result.append(i)

    return result


array: List[int] = [7, 3, 0, 1, 5, 2, 5, 19, 10, 5]
sorted_array = counting_sort(array)
print(sorted_array)
