class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:

        count = {}
        ans = []
        for num in nums:
            count[num] = count.get(num , 0)+1
            if count[num] == 2:
                ans.append(num)

        return ans