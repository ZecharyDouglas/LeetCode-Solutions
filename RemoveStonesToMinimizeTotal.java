class Solution {
    
    //create a max heap and add the piles elements to it 
    //run the function k times and have it return the sum of all the element at the end
    public int minStoneSum(int[] piles, int k) {
        PriorityQueue<Integer> stones = new PriorityQueue<>(Comparator.reverseOrder());
        for(int n : piles){      
            stones.add(n);
        }
        
        for (int i=0;i<k;i++){
            int newVal = stones.remove();
            newVal= (int) Math.floor(newVal - (newVal/2));
            stones.add(newVal);
        }
        
        int sum=0;
        
        for(int i=0;i<piles.length;i++){
            sum+=stones.remove();
        }
        return sum;
        
    }
}