class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #sort each string in strs individually and map it to its original word
        # sorted version -> original word 
        # return the values of the map
        word_map={}
        for word in strs:
            
            srted=str(sorted(word))
            if srted not in word_map:
                word_map[srted]=[]
                word_map[srted].append(word)
            else:
                word_map[srted].append(word)
        print(word_map)
        return list(word_map.values())
