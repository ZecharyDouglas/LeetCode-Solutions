from collections import Counter , OrderedDict
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        #add all elements to a map sorted by frequencies
        #compute the min needed elements to meet return condition
        #iterate through values of the map (prefix sum) until condition is met
        #return answer
        sortedMap = OrderedDict(Counter(arr).most_common())
        minNeededSum=len(arr)/2
        prefixSum=0
        ans=0
        for key , value in sortedMap.items():
            prefixSum+=value
            ans+=1
            if prefixSum >= minNeededSum:
                return ans
        return ans
    