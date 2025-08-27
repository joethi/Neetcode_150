from typing import Optional
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr, prev = head, None
        while curr.next:
            temp = curr.next 
            curr.next = prev
            prev = curr
            curr = temp

        return prev 

head = ListNode(0, ListNode(1, ListNode(2, ListNode(3, None))))
sol_obj = Solution()
print(sol_obj.reverseList(head))


