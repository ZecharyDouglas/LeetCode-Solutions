class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxAltitude=0
        altitude=0
        for i in range(len(gain)):
            altitude+=gain[i]
            maxAltitude = max(maxAltitude , altitude)
        return maxAltitude