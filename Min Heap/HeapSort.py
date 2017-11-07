from MinHeap import *

def fake_heap_sort(arr):
    heap = MinHeap()
    for elem in arr:
        heap.insert(elem)
    arr = []
    while not heap.is_empty():
        arr.append(heap.peek())
        heap.delete()
    return arr

