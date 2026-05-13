# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        dummy=head
        
        #I can add the entire node to a hash map / set
        while dummy is not None:
            if dummy not in visited:
                visited.add(dummy)
                dummy = dummy.next
            else:
                return True
            
        return False