from collections import deque
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #answer[i]==product of elements 0->i * product of elements i+1->n
        #left prefix product array beginning with first element 1
        #right prefix product begins with first element 1 from the right side of the list
        n = len(nums)
        
        left = [1] * n
        right = [1] * n
        ans = [1] * n
        
        # build left
        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]
        
        # build right
        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]
        
        # build answer
        for i in range(n):
            ans[i] = left[i] * right[i]
        
        return ans