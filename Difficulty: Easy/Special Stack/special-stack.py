import sys
def push(arr, ele):
    arr.append(ele)

# Function should pop an element from stack
def pop(arr):
    if arr:
        return arr.pop()
    return -1

# function should return 1/0 or True/False
def isFull(n, arr):
    return True if n==len(arr) else False

# function should return 1/0 or True/False
def isEmpty(arr):
    return 1 if len(arr)==0 else 0

# function should return minimum element from the stack
def getMin(n, arr):
    if not arr:
        return
    mini=sys.maxsize
    while arr:
        mini=min(mini,arr.pop())
    return mini