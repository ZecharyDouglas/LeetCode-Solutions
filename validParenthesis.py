class Solution:
    def isValid(self, s: str) -> bool:
        brackets={
            ")":"(",
            "}":"{",
            "]":"["
        }
        stack =[]
        count=0
        if len(s) < 2:
            return False

        while count < len(s):
            if s[count] in brackets:
                if len(stack)>=1 and brackets[s[count]] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[count])
            count+=1

        if len(stack) >0:
            return False

        return True
        