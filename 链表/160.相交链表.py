# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
方法1：双指针
思路：a + m + b == b + m + a ; m 为链表相交部分

时间复杂度：O(n)
空间复杂度：O(1)

"""

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        q = headA
        p = headB
        while (q != p):
            q = q.next if q else headB
            p = p.next if p else headA
        return q
        