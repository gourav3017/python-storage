class MinHeap:
    def __init__(self, size = 0):
        self.data = ['']
        self.size = 0
    def __str__(self):
        return str(self.data[1:])
    def clear_heap(self):
        self.data = []
        self.size = 0
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
