# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        string=[]
        dummy=head
        while dummy is not None:
            string.append(dummy.val)
            dummy=dummy.next
        clone=string[::-1]
        print(clone)
        print(string)
        if clone == string:
            return True
        return False