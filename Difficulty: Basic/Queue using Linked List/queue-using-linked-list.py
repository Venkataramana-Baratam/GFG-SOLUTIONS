# A linked list (LL) node to store a queue entry
class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None

class MyQueue:
    
    def __init__(self):
        self.start = None
        self.end = None
        self.size = 0
    
    # Function to push an element into the queue
    def push(self, item):
        temp = Node(item)  # Fixed Newnode -> Node
        
        if self.start is None:  # Queue is empty
            self.start = temp
            self.end = temp
        else:
            self.end.next = temp
            self.end = temp
        
        self.size += 1  # Fixed size -> self.size

    # Function to pop front element from the queue
    def pop(self):
        if self.start is None:
            return -1  # Return something when queue is empty

        temp = self.start
        self.start = self.start.next
        popped_value = temp.data
        del temp
        self.size -= 1

        if self.start is None:  # If queue becomes empty
            self.end = None
        
        return popped_value
