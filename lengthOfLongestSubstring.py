class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        longestSubstring=0
        stringset=set()
        for right in range(len(s)):
            while s[right] in stringset:
                stringset.remove(s[left])
                left+=1
            stringset.add(s[right])
            temp = (right - left ) + 1
            longestSubstring = max ( temp , longestSubstring )
        return longestSubstring