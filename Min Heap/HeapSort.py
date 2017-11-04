from MinHeap import *

def heap_sort(arr):
    heap = MinHeap()
    for elem in arr:
        heap.insert(elem)
    arr = []
    while not heap.empty():
        arr.append(heap.pop)
    return arr

