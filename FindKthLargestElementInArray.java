class Solution {
    public int findKthLargest(int[] nums, int k) {
        //min heap 
        //add all and if bigger than k remove from the heap 
        PriorityQueue<Integer> heap = new PriorityQueue<>();
        for(int n : nums){
            heap.add(n);
            if(heap.size()>k){
                heap.remove();
            }
        }
        return heap.peek();
    }
}
