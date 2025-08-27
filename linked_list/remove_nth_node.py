# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head
        while n > 0 and right:
            right = right.next
            n -= 1
        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummy.next 
    
head = [1,2,3,4]
n = 2
lnkd_lst = ListNode(val = 1, next = ListNode(val = 2, next = ListNode(val=3, next = ListNode(val=4))))
sol_obj= Solution()
result = sol_obj.removeNthFromEnd(lnkd_lst, n)    
print(result.val)

