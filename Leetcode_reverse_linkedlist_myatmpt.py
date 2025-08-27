# Definition for singly-linked list.
class NodeList:
    def __init__(self, val = 0 , next = None):
        self.val = val
        self.next = next    

class Solution: 
    def reverse_linked_list(self, head: NodeList) -> NodeList:
        prev, curr = None, head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr    
            curr = temp                              
        return prev
                         
