def counting_sort(array: list):
    max_number = 100
    occurrences = [0 for _ in range(max_number + 1)]

    for number in array:
        occurrences[number] += 1

    array.clear()
    for i in range(len(occurrences)):
        for j in range(occurrences[i]):
            array.append(i)


array = [7, 3, 0, 1, 5, 2, 5, 19, 10, 5]
counting_sort(array)
print(array)
