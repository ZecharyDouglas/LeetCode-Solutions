class Solution:

    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float('inf')
        second = float('inf')
        #finds the two smallest numbers and if the current element is not the smallest or second smallest numbers so far, then it the third element of the triplet
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False