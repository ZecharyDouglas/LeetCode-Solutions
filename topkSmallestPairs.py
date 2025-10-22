import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []

        heap = []
        # push initial pairs (nums1[i], nums2[0])
        for i in range(min(k, len(nums1))):
            heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))
        
        ans = []
        while heap and len(ans) < k:
            total, i, j = heapq.heappop(heap)
            ans.append([nums1[i], nums2[j]])

            # move to next element in nums2 for same nums1[i]
            if j + 1 < len(nums2):
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))

        return ans