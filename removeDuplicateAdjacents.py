class Solution:
    def removeDuplicates(self, s: str) -> str:
        #no existing duplicates 
        #existing duplicates
        #two pointers 
        # s = list(s)
        # if len(s) < 2:
        #     return s
        
        # left = 0
        # right = 1
        # while right < len(s):
        #     if s[left] == s[right]:
        #         del s[left:right+1]
        #         left=0
        #         right=1
        #         continue
            
        #     left+=1
        #     right+=1
        # s = "".join(s)
        # return s
        #### time limit exceded O(n^2)

        stack = []
        for ch in s:
            if stack and stack[-1] == ch:
                stack.pop()        # remove the pair
            else:
                stack.append(ch)   # keep it
        return "".join(stack)