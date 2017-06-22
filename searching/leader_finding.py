def find_leader(array):
    counter = 0
    for i in range(0, len(array)):
        if counter == 0:
            current_candidate = array[i]
            counter = 1
        else:
            if array[i] == current_candidate:
                counter += 1
            else:
                counter -= 1

    return current_candidate


array = [1, 2, 5, 5, 7, 5, 5, 10, 5, 5]
majority = find_leader(array)
print(f'Majority element is: {majority}')
