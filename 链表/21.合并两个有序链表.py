# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
思路1：迭代比较L1和L2的值
'''
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(None)
        head = res
        while l1 and l2:
            if l1.val > l2.val:
                head.next = l2
                l2 = l2.next 
            else:
                head.next = l1
                l1 = l1.next
            head = head.next
        if l1:
            head.next = l1
        else:
            head.next = l2
        return res.next