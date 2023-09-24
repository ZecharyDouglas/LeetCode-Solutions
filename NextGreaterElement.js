//Beats 26.02 at time of sub for time comp and 45% for memory distribution
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var nextGreaterElement = function (nums1, nums2) {
  //for each number in the nums1 array , find the corresponding element and its index in nums2
  //iterate from the corresponding index in nums 2 until a larger integer is found or -1 is returned
  //add the query result to the answer array and then return the array
  let ans = [];
  for (const element of nums1) {
    let query = nums2.findIndex((num) => num == element);
    let arrLen = ans.length;
    for (let i = query; i < nums2.length; i++) {
      if (nums2[i] > element) {
        ans.push(nums2[i]);
        break;
      }
    }
    if (ans.length === arrLen) {
      ans.push(-1);
    }
  }
  return ans;
};
