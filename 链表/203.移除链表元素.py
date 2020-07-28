# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
方法1：哨兵节点
思路：删除链表中间节点非常简单，让slow.next = fast.next即可；但是如果要删除一个或多个节点位于链表头部时，事情会变的复杂
哨兵节点的主要目的：标准化链表，让链表永不为空，永不无头，简化插入和删除

时间复杂度：O(n)
空间复杂度：O(1)
"""

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        sentinel = ListNode(0)
        sentinel.next = head
        
        slow,fast = sentinel,head
        while fast:
            if fast.val == val:
                slow.next = fast.next
            else:
                slow = slow.next
            fast = fast.next
        return sentinel.next