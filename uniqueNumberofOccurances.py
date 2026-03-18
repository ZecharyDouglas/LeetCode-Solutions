from collections import defaultdict
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        #add all the elements of the arr to a dictionary
        #iterate through the values and add them to a set,
            #while addin to the set check for previous existence
        my_map=defaultdict(int)
        my_set=set()
        for num in arr:
            my_map[num]+=1

        for num in my_map.values():
            if num not in my_set:
                my_set.add(num)
            else:
                return False
        return True