# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # None  0 -> 1 -> 2 -> 3

        if head == None:
            return head
        else:
            curr = head
            prev = None
            nex = curr.next


        

        while curr != None:
            # None <- 0  1 -> 2 -> 3
            # Edge(0,None)
            # prev = 0
            # curr = 1
            curr.next = prev
            prev = curr
            curr = nex
            # nex = 2
            if curr == None:
                return prev
            else:
                nex = curr.next

        
            

        