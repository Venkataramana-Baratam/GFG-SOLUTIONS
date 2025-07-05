class MyStack:
    
    def __init__(self):
        self.arr=[]
        self.top = -1
        self.size = 1000
        self.arr = [0]*self.size
    #Function to push an integer into the stack.
    def push(self,data):
        #add code here
        self.top+=1
        self.arr[self.top] = data
    
    #Function to remove an item from top of the stack.
    def pop(self):
        #add code here
        if self.top==-1:
            return -1
        x = self.arr[self.top]
        self.top -=1
        return x
        
        
        