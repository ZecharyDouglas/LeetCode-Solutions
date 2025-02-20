from heapq import *

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        #convert piles into a heap
        #take the largest pile and perform floor divsion operation 
        #repeat the operation k times 
        #perform a summing operation on the elements of the heap and then return the sum value
        
       
        heap = [-pile for pile in piles]
        heapq.heapify(heap)
        while k > 0:
            largest = heapq.heappop(heap)
            largest=abs(largest)
            replacement = largest - (largest // 2)
            replacement *=-1
            heapq.heappush(heap , replacement)
            k-=1
        return sum(map(abs, heap))