# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

""" 
思路1：先让前置节点移动k次，然后同时移动前置和后置节点，当前置节点为NULL时，返回后置节点即可
"""
class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        former = latter = head
        for _ in range(k):
            former = former.next
        while former:
            former = former.next
            latter = latter.next     
        return latter