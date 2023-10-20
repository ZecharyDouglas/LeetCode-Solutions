import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class ReduceArraySizeToTheHalf {
    class Solution {
    public int minSetSize(int[] arr) {
        //create a hashmap and add the values mapped to their frequency 
        //sort the list from greatest to least 
        Map<Integer , Integer> map = new HashMap<>();
        
        for(int x : arr){
            map.put(x , map.getOrDefault(x , 0)+1);
        }
        
        List<Map.Entry<Integer , Integer>> sortedMap = new ArrayList <>(map.entrySet());
        sortedMap.sort(Map.Entry.<Integer, Integer>comparingByValue().reversed());
        
        
        int length = arr.length;
        int count=0;
        
         for (Map.Entry<Integer, Integer> entry : sortedMap) {
            length -= entry.getValue();
            count++;
            if (length <= arr.length / 2) {
                return count;
            }
        }
        return count;
        
        }
    }

}
