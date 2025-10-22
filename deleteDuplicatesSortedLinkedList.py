# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        dummy = head
        
        while curr:
            next_node = curr.next
            while next_node and curr.val == next_node.val:
                next_node=next_node.next
            curr.next = next_node
            curr = next_node
            if next_node:
                next_node = next_node.next
        return dummy
            