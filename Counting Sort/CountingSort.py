def counting_sort(arr):
    if len(arr) == 0:
        return arr

    def get_max(arr):
        max_elem = arr[0]
        for elem in arr:
            if elem > max_elem:
                max_elem = elem
        return max_elem

    def get_min(arr):
        min_elem = arr[0]
        for elem in arr:
            if elem < min_elem:
                min_elem = elem
        return min_elem

    def step_up(arr):
        for index in range(len(arr) - 1):
            arr[index + 1] += arr[index]
        return arr

    min_number = get_min(arr)
    max_number = get_max(arr)
    count = [] # count[0]: min_number, count[i]: min_number + i
    for _ in range(max_number - min_number + 1):
        count.append(0)

    for number in arr:
        count[number - min_number] += 1
    count = step_up(count)

    new_arr = []
    for _ in range(len(arr)):
        new_arr.append(0)

    for number in arr:
        new_arr[count[number - min_number] - 1] = number
        count[number - min_number] -= 1
    return new_arr

