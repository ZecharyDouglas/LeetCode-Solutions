/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function (nums, val) {
  //go through all elements of the array to find all occurences of val
  //swap elements with elements at the end
  //set the length of the array
  //move left back 1 incase both of the swapped elements need to be removed
  let right = nums.length - 1;
  for (let left = 0; left < nums.length; left++) {
    if (nums[left] == val) {
      [nums[left], nums[right]] = [nums[right], nums[left]];
      nums.length = nums.length - 1;
      right--;
      left--;
    }
  }
  return nums.length;
};
