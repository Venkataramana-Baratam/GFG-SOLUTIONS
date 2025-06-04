class Solution:
    def mergeSort(self, head):
        if head is None or head.next is None:
            return head
        values = []
        temp = head
        while temp:
            values.append(temp.data)
            temp = temp.next
        values.sort()
        temp = head
        for val in values:
            temp.data = val
            temp = temp.next

        return head
