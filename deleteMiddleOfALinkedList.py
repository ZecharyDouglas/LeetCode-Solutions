# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head
        n=0
        while dummy:
            n+=1
            dummy=dummy.next
        if (n)==1:
            return 
        n=(n//2-1)
        dummy=head
        for _ in range(n):
            dummy=dummy.next
        next_node=dummy.next
        next_node=next_node.next
        dummy.next=next_node

        return head