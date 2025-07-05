class MyStack:


    # class StackNode:

    # # Constructor to initialize a node
    # def __init__(self, data):
    #     self.data = data
    #     self.next = None
        
    #Function to push an integer into the stack.
    def __init__(self):
        self.top = None
        self.size = 0
        
        
        
        
        
    def push(self, data):

        # Add code here
        
        temp = StackNode(data)
        temp.next = self.top
        self.top = temp
        self.size +=1


    #Function to remove an item from top of the stack.
    def pop(self):

        # Add code here
        if self.top is None:
            return -1  # or raise an exception

        popped_node = self.top
        self.top = self.top.next
        popped_data = popped_node.data
        del popped_node
        self.size -= 1
        return popped_data