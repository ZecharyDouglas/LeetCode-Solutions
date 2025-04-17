class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        result=0
        #greedy check that starts at an index and checks if the minimum is possible , as well as satisfying 
        #the minimum number of pieces 
        def checkSweetness(minSweetness):
            total = 0
            pieces=0
            for s in sweetness:
                total+=s
                if total >=minSweetness:
                    total = 0
                    pieces+=1
            return pieces >= k+1
        
        left = min(sweetness)
        right = sum(sweetness)
        #binary search on the solution space
        while left <= right:
            mid = (left + right )//2
            if checkSweetness(mid):
                result=mid
                left = mid+1
            else:
                right = mid -1
        return result
                


        