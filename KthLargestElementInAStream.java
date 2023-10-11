//beats 91% of solutions at time of sub
//java solution////
class KthLargest {
    public int k;
    public PriorityQueue<Integer> heap;
    public KthLargest(int k, int[] nums) {
        this.k = k;
        this.heap = new PriorityQueue<>(k);
        for(int num : nums){
            add(num);
        }
    }
    
    public int add(int val) {
        if(heap.size()<k){
            heap.add(val);
        }
        else if(heap.peek() < val){
            heap.remove();
            heap.add(val);
        }
        return heap.peek();
    }
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest obj = new KthLargest(k, nums);
 * int param_1 = obj.add(val);
 */