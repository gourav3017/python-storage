def radix_sort_LSD(arr):
    if len(arr) == 0:
        return arr

    def get_max(arr):
        max_elem = arr[0]
        for elem in arr:
            if elem > max_elem:
                max_elem = elem
        return max_elem
    round_down = lambda number, exp: number // exp # eg. 802, 10: 80
    truncate = lambda number: number % 10 # eg. 802: 2

    def sort_once(arr, exp):
        bucket = [[], [], [], [], [], [], [], [], [], []]
        # note. bucket = [[]] * 10 does NOT work
        for index in range(len(arr)):
            bucket[truncate(round_down(arr[index], exp))].append(arr[index])
        arr = []
        for row in bucket:
            for number in row:
                arr.append(number)
        return arr

    exp = 1
    max_number = get_max(arr)
    while max_number // exp != 0:
        arr = sort_once(arr, exp)
        exp *= 10
    return arr

