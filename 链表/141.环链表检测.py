# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
思路1：用哈希表保存每个Node的引用（或内存地址）；然后遍历链表，判断每个Node是否存在于哈希表中

时间复杂度：O(n)
空间复杂度：O(n)
'''
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # 声明一个集合
        set1 = set()
        while head:
            if head in set1:
                return True
            set1.add(head)
            head = head.next
        return False

'''
思路2：快慢指针；一个快指针每次移动2个Node，一个慢指针每次移动1个Node，如果快指针和慢指针相遇的时候，则链表有环

时间复杂度：O(n)
空间复杂度：O(1)
'''
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast = slow = head
        # 如果 head为空 || fast指针为空
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            while fast is slow:
                return True
        return False