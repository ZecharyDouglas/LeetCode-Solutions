import java.util.PriorityQueue;

public class MinimumCostToConnectSticks {
    class Solution {
    public int connectSticks(int[] sticks) {
        //min queue 
        //function that removes twice and sums , then add back to queue
        //return final result 
        
        if(sticks.length==1)
            return 0;
        
        PriorityQueue <Integer> heap = new PriorityQueue<>();
        
        for(int x:sticks){
            heap.add(x);
        }
        
        int cost=0;
        
        while(heap.size()>1){
            int sum=0;
            sum+=heap.remove();
            sum+=heap.remove();
            heap.add(sum);
            cost+=sum;
        }
        return cost;
    }
}
}
