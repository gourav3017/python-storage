from Node import Node
class LinkedList(object):
    def __init__(self, head = None):
        self.head = head
    def push(self, data):
        new_node = Node(data)
        # Set the new node pointing to the original first node
        new_node.next = self.head
        # Set the head pointer pointing to the new node
        self.head = new_node
    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count
    def search(self, data):
        current = self.head
        position = None
        while current:
            if current.data == data:
                position = current
                break
            else:
                current = current.next
        return current
    def __str__(self):
        current = self.head
        string = '['
        while current:
            string += str(current.data)
            if current.next:
                string += ','
            current = current.next
        string += ']'
        return string
    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.data == data:
                found = True
                break
            else:
                previous = current
                current = current.next
        if current is None:
            raise ValueError('Data not in list')
        if previous is None:
            # Target data shows up at first element
            self.head = current.next
        else:
            previous.next = current.next
    def attach(self, data):
        current = self.head
        while current.next:
            # Find the last element in the list
            current = current.next
        new_node = Node(data)
        current.next = new_node
    def deleteAll(self, data):
        while self.search(data) is not None:
            self.delete(data)
    def itemAt(self, index):
        # Return element at a position in the list
        if index >= self.size():
            raise IndexError('Sequence index out of range')
        current = self.head
        current_index = 0
        while current_index < index:
            current = current.next
            current_index += 1
        return current.data
    def reverse(self):
        current = self.head
        previous = None
        while current:
            # Store the next item for successful looping
            temp = current.next
            current.next = previous
            previous = current
            current = temp
        self.head = previous
