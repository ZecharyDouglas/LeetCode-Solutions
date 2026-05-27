class Solution:
    def countAndSay(self, n: int) -> str:
        arr="1"
        #move to the next element in the string
        if n == 1:
            return arr 
        #between indexes 1 and n 
            #count repeated occurances of a character, add the occurances with count / char to ans list
        for _ in range(n-1):
            i=0
            ans=[]
            while i < len(arr):
                curr = arr[i]
                count=0
                while i < len(arr) and arr[i] == curr :
                    count+=1
                    i+=1
                ans.append(str(count))
                ans.append(curr)
        #join the array into a string at the end
            arr = "".join(ans)

        
        return arr