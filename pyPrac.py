import os
def compress(input):
    s=[]
    i=0
    while i < len(input):
        curr=input[i]
        count=0
        while i < len(input) and input[i]==curr:
              count+=1
              i+=1
        s.append(curr)
        s.append(str(count))
    
    return "".join(s)


# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.
def two_sum(nums , target):
        counter={}
        for i in range(len(nums)):
            difference=target-nums[i]
            if difference in counter:
                ans = counter.get(difference)
                return [ans , i]
            else:
                counter[nums[i]]=i
                
                  
        
def valid_palindrome(s):
    pass
def max_subarray(nums):
    pass
def nearest_exit(grid , start):
    pass
if __name__ == '__main__':
    compress()