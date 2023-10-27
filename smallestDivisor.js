/**
 * @param {number[]} nums
 * @param {number} threshold
 * @return {number}
 */
var smallestDivisor = function (nums, threshold) {
  //create a binary search that will make a divisor between 1 and the max value in the nums array
  //check function that tests the divisor against the threshold

  let check = (test) => {
    let sum = 0;
    for (let num of nums) {
      sum += Math.ceil(num / test);
    }
    return sum <= threshold;
  };
  let left = 1;
  let right = Math.max(...nums);
  while (left <= right) {
    let mid = Math.floor((left + right) / 2);
    if (check(mid)) right = mid - 1;
    else left = mid + 1;
  }
  return left;
};
