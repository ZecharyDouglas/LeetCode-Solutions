import java.util.PriorityQueue;

public class MaximumUnitsOnATruck {
    class Solution {
    public int maximumUnits(int[][] boxTypes, int truckSize) {
        //product of boxes and units are a set 
        //hash map of each index of boxtype array mapped to the set 
        //max heap for the collection
        //if the set can fit, remove from heap and decrement truckSize by the removed value 
        PriorityQueue<int[]> heap = new PriorityQueue<>((a , b)->b[1]-a[1]);
        for(int[]x : boxTypes){
            heap.add(x);
        }
        int totalUnits=0;
        
        while(truckSize > 0 && !heap.isEmpty() ){
          int[] box = heap.remove();
           int boxes = Math.min(truckSize, box[0]);
            totalUnits += boxes * box[1];
            truckSize -= boxes;
        }
        return totalUnits;
    }
}
}
