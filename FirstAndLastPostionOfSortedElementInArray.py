class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        #binary search for the target number
        #if found 
        #while loop with two pointers that epxands outwards while the current elemnts are equal to the target element
        #if not found return [-1.-1]

        #binary search
        left =0
        right = len(nums)-1
        found = [-1 , -1]
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                found = [middle , middle]
                break
            elif nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1
        left , right = found
        if found != [-1 , -1]:
            while nums[left] == target or nums[right]==target:
                if right+1 < len(nums) and nums[right+1]==target:
                    right+=1
                elif left-1 >= 0 and nums[left-1]==target:
                    left-=1
                else:
                    break
            found = left , right
        return found