class Solution:
    def reverseWords(self, s: str) -> str:
        #iterate through the string , while current character not equal to " " add to a word array
        #if current character == " " make word array into a string and push onto stack with the space
        #at end of the list pop until empty , 
        # arr = s.split()
        # ans=[]
        ###
        # for i in range(len(arr)):
        #     if i != len(arr)-1:
        #         ans.append(arr[i])
        #         ans.append(" ")
        #     else:
        #         ans.append(arr[i])
        # ans.reverse()
        # return "".join(ans)

        ##alternate version one liner
        return " ".join(s.split()[::-1])
