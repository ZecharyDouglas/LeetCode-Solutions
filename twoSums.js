/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  //use a hash map and map an element's complement to its index
  let map = new Map();
  let ans = [];
  for (let i = 0; i < nums.length; i++) {
    //compute complement
    let complement = target - nums[i];
    //lookup  current element
    if (map.has(nums[i])) {
      //if found return the index(value) of associated complement and the current index in the iteration
      ans.push(map.get(nums[i]));
      ans.push(i);
      return ans;
    }
    //else add complement and its index to the map
    map.set(complement, i);
  }
  return ans;
};
