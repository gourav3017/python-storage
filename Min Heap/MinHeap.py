# This algorithm heapifies the entire binary tree
# This function is NOT pure
def min_heapify(data):
    def heapify_util(data, index):
        left = index * 2
        right = left + 1
        min_index = index
        if left <= len(data) - 1:
            if data[left] < data[min_index]:
                min_index = left
        if right <= len(data) - 1:
            if data[right] < data[min_index]:
                min_index = right
        if min_index != index:
            data[index], data[min_index] = \
            data[min_index], data[index]
            heapify_util(data, min_index)
    for index in range(len(data) - 1):
        heapify_util(data, len(data) - 1 - index)

class MinHeap:
    def __init__(self):
        self.data = ['']
        self.size = 0
    def __str__(self):
        return str(self.data[1 : self.size + 1])
    def __len__(self):
        return self.size
    def clear(self):
        self.data = ['']
        self.size = 0
    def is_empty(self):
        return self.size == 0
    def peek(self):
        return self.data[1]
    def insert(self, value):
        def bubble_up(index):
            if index == 1:
                return
            parent = index // 2
            if self.data[parent] > self.data[index]:
                self.data[parent], self.data[index] = \
                self.data[index], self.data[parent]
                bubble_up(parent)
        self.size += 1
        self.data.append(value)
        bubble_up(self.size)
    def delete(self):
        if self.size == 0:
            raise ValueError("heap is empty")
        def bubble_down(index):
            left = index * 2
            right = left + 1
            if left > self.size and right > self.size:
                return
            if right > self.size or self.data[right] >= self.data[left]:
                if self.data[left] < self.data[index]:
                    self.data[left], self.data[index] = \
                    self.data[index], self.data[left]
                    bubble_down(left)
            else:
                if self.data[right] < self.data[index]:
                    self.data[right], self.data[index] = \
                    self.data[index], self.data[right]
                    bubble_down(right)
        self.data[1] = self.data[self.size]
        del self.data[self.size]
        self.size -= 1
        bubble_down(1)

