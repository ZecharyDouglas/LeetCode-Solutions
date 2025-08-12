def longestCommonPrefix(self, strs: List[str]) -> str:
        #answer array
        #get the shortest word , generate an index to iterate by index of the shortest word against every other word
        #if not equal at same index for all words , return current ans array as string

        ans = []
        shortestWord= min(strs , key=len)
        print(shortestWord)
        for index in range(len(shortestWord)):
            for word in strs:
                if word[index] != shortestWord[index]:
                    return "".join(ans)
            ans.append(shortestWord[index])
        return shortestWord