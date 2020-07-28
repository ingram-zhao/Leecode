# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
思路1：快慢指针
    fast指针每次移动2步，slow指针每次移动1步，当fast指针走到最后的时候，返回slow即为中间节点

"""
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow