# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
思路：curr指针指向当前节点，每次将 curr.next 指向前一个 Node 
'''
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None 
        curr = head
        while curr:
            tmp = curr.next 
            curr.next = pre
            pre = curr
            curr = tmp
        return pre