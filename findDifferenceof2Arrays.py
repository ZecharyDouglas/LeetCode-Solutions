class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        #2d ans array
        #2 sets , one for each list , iterate through both , 
        #for each element if opposite set !contains element push to correct answer array
        answer=[[],[]]
        l1=set()
        l2=set()
        for i in nums1:
            l1.add(i)
        for i in nums2:
            l2.add(i)
        for num in l1:
            if num not in l2:
                answer[0].append(num)
        for num in l2:
            if num not in l1:
                answer[1].append(num)
        return answer