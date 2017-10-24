def counting_sort(array):
    occurrences = []
    for i in range(0, 101):
        occurrences.append(0)

    for number in array:
        occurrences[number] += 1

    result = []
    for i in range(0, len(occurrences)):
        for j in range(0, occurrences[i]):
            result.append(i)

    return result


array = [7, 3, 0, 1, 5, 2, 5, 19, 10, 5]
sorted_array = counting_sort(array)
print(sorted_array)
