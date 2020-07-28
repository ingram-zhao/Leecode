# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
方法1：栈
思路：
    1. 先遍历一遍链表并将Node加入到stack中
    2. 从stack中弹出Node的同时再遍历一遍链表
    3. 比较弹出的Node和遍历的Node值是否相等

时间复杂度：O(n)
空间复杂度：O(n)
"""
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        stack = []
        curr = head
        while curr:
            stack.append(curr)
            curr = curr.next
        node1 = head
        while stack:
            node2 = stack.pop()
            if node2.val != node1.val:
                return False
            node1 = node1.next
        return True

"""
方法2：反转
思路：
    1. fast和slow指针，slow指针边遍历边反转，当fast指针到尾部的时候前半部分已经反转
    2. node1和node2指针从链表中间分别向两边移动，并比较是否相等

时间复杂度：O(n)
空间复杂度：O(1)
"""
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        fast = slow = head
        pre = None 
        while fast and fast.next:
            fast = fast.next.next
            tmp = slow.next
            slow.next = pre
            pre = slow
            slow = tmp
        if fast:
            node1 = pre
            node2 = slow.next
        else:
            node1 = pre
            node2 = slow
        while node1 and node2:
            if node1.val != node2.val:
                return False
            node1,node2 = node1.next,node2.next
        return True