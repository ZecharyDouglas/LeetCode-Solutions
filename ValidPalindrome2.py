def validPalindrome(self, s: str) -> bool:
        # use a single loop and check if the string is a palindrome 
        # if a mismatch is encountered then start a new check for palindrome validity
        # using a function called on both ends of the string

        left = 0
        right =len(s)-1
        ans=True
        if len(s) <= 1:
            return False

        def checkValidPalindrome(l , r):
            while l<r:
                if s[l]!= s[r]:
                    return False
                l+=1
                r-=1
            return True

        
        
        while left < right:
            if s[left] != s[right]:
                return checkValidPalindrome(left+1, right) or checkValidPalindrome(left , right-1)
                
            left+=1
            right-=1
        return True