public class SearchInsertPosition {
    class Solution {
        public int searchInsert(int[] nums, int target) {
            //binary search that returns the left at the end if the element is not found and the index if it is found
            int left=0;
            int right=nums.length-1;
            while(left<=right){
                int mid = left + (right-left)/2;
                
                if(nums[mid]==target){
                    return mid;
                }
                if(nums[mid]>target){
                    right=mid-1;
                }
                else{
                    left=mid+1;
                }
                
            }
            return left;
        }
    }
}
