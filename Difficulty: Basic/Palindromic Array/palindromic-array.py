def isPalinArray(arr):
    # check each number
    for num in arr:
        s = str(num)              # convert to string
        if s != s[::-1]:          # if not palindrome
            return False
    return True
