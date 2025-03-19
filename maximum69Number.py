class Solution:
    def maximum69Number (self, num: int) -> int:
        #convert the number to a string 
        #split the string into an array of elements
        #iterate through the string and look for the first instance of a 6 and then change it to a 9
        #convert the array back into a string and then into a number 
        #return
        num = str(num)
        num = list(num)
        for i in range(len(num)):
            if num[i] == '6':
                num[i] = '9'
                break
        num = "".join(num)
        return int(num)