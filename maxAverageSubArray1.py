class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        #two pointers sliding window size k 
        #answer variable that is updated if greater than current
        left=0 
        right=0
        ans=float("-inf")
        sumvar=0
        while right < len(nums):
            #expand window
            while right - left + 1 <= k:
                sumvar += nums[right]
                right += 1
            #compute average for given window
            avg = sumvar / k
            #update answer variable if necessary
            if avg > ans:
                ans = avg
            #iterate function from the left
            sumvar -= nums[left]
            left+=1
           
        return ans