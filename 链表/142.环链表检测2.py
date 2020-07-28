# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
方法1：哈希表
思路：...
时间复杂度：O(n)
空间复杂度：O(n)
"""


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        set1 = set()
        curr = head
        while curr is not None:
            if curr in set1:
                return curr
            else:
                set1.add(curr)
                curr = curr.next
        return None 
        