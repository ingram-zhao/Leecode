# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""
思路：利用两个指针，先找到要删除Node的前一个Node，让这个Node指向下下个节点
时间复杂度：O(n)
空间复杂度：O(1)
"""

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        former = latter = head
        for _ in range(n+1):
            if former:
                former = former.next
            else:
                return head.next
        while former:
            former = former.next
            latter = latter.next
        latter.next = latter.next.next
        return head