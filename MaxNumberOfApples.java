import java.util.Arrays;

public class MaxNumberOfApples {
    
    class Solution {
    public int maxNumberOfApples(int[] weight) {
        //sort weight in place and remove from max weight while incrementing count for each apple added
        
        Arrays.sort(weight);
        
        int max=5000;
        int count=0;
        for(int i=0;i<weight.length;i++){
            int apple = weight[i];
            if(max-apple>=0){   
            count++;
            max-=apple;
            }
            else
                return count;
        }
        return count;
    }
}
}
