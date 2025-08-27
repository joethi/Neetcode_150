# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy, node = ListNode()
        while list1 and list2:
            if list1.val > list2.val:
                node.next = list2
                list2 = list2.next
            else:
                node.next = list1
                list1 = list1.next
            node = node.next            
        node.next = list1 or list2
        return dummy.next
        
lnkd_lst1 = ListNode(val = 1, next = ListNode(val = 2, next = ListNode(val = 4)))
lnkd_lst2 = ListNode(val = 1, next = ListNode(val = 3, next = ListNode(val = 5)))
sol_obj= Solution()
result = sol_obj.mergeTwoLists(lnkd_lst1, lnkd_lst2)




