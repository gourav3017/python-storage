def bubble_sort(arr):
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]
    is_sorted = False
    last = len(arr) - 1
    while not is_sorted:
        is_sorted = True
        for index in range(0, last):
            if arr[index] > arr[index + 1]:
                swap(index, index + 1)
                is_sorted = False
        last -= 1
    return arr

