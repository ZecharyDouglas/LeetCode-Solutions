class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        #iterate through list
        #if current element is 0 , the element previous and after exists and is also 0 n-1
        #if n==0 at end return true else return false

        for i in range(len(flowerbed)):
            #single element array
            if len(flowerbed)==1:
                if flowerbed[i]==0:
                    flowerbed[i]=1
                    n-=1
            #if current element is 0 and i ==0 check next and flip current to i
            if flowerbed[i] == 0 and i == 0 and flowerbed[i+1] == 0:
                flowerbed[i]=1
                n-=1
            #if current element is 0 i ==last element check prev and flip current to i
            elif flowerbed[i]==0 and i == len(flowerbed)-1 and flowerbed[i-1] == 0:
                flowerbed[i]=1
                n-=1
            #if both left and right are 0 make current one 
            elif flowerbed[i]==0 and flowerbed[i-1]==0 and flowerbed[i+1]==0:
                flowerbed[i]=1
                n-=1
                
        if n<=0:
            return True
        else:
            return False