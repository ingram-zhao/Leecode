# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
方法1：
思路：将奇节点放到一个链表里，偶节点放到另一个链表里，然后把偶链表接在奇链表的尾部

时间复杂度：O(n)
空间复杂度：O(1)
"""

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None: return None
        odd = head
        evenhead = even = head.next
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenhead
        return head