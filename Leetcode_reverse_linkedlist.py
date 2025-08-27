# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

# head = [0,1,2,3]
# O_3 = ListNode(3)
# print("O_3.val: ", O_3.val)
# print("O_3.next: ", O_3.next)

# O_2 = ListNode(2, ListNode(3))
# print("O_2.val: ", O_2.val)
# print("O_2.next: ", O_2.next)
# print("O_2.next.next: ", O_2.next.next)

head = ListNode(0, ListNode(1, ListNode(2, ListNode(3))))

sol_obj = Solution()
rev_lnk_lst = sol_obj.reverseList(head)
print("rev_lnk_lst: ", rev_lnk_lst)
