/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function (nums) {
  //add elements to a set to remove duplicates automatically
  //remove elements from the nums array by setting the length to 0
  //add the elements back from the set into the array and return the length
  let set = new Set();
  for (let num of nums) {
    set.add(num);
  }
  nums.length = 0;
  set.forEach((num) => nums.push(num));
  return nums.length;
};
