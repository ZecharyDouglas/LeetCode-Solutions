class Solution:
    def reverseVowels(self, s: str) -> str:
        #set containing all vowels uppercase/lowercase O(1) lookup
        #two pointers iterating from opposite ends of the list
            #while they dont cross eachother 
                #two while loops that increment till they find a vowel
                #swap elements
                #increment pointers
        s=list(s)
        m_set=set()
        left=0
        right=len(s)-1
        #adding all vowels to the set
        m_set.add('a')
        m_set.add('e')
        m_set.add('i')
        m_set.add('o')
        m_set.add('u')
        m_set.add('A')
        m_set.add('E')
        m_set.add('I')
        m_set.add('O')
        m_set.add('U')

        while left < right:
            #while loop to increment left pointer
            while left < right and s[left] not in m_set:
                left+=1
            #while loop to decrement right pointer
            while left < right and s[right] not in m_set:
                right-=1
            #swap step
            s[left] , s[right] = s[right] , s[left]
            #move pointers
            left+=1
            right-=1
        return "".join(s)