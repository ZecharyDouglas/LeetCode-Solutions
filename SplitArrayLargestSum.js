/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var splitArray = function (nums, k) {
  let largestSum = Math.floor(
    nums.reduce((acc, num) => {
      return acc + num;
    }, 0)
  );
  let check = (maxSum) => {
    let sum = 0;
    let count = 1;
    for (let i = 0; i < nums.length; i++) {
      if (sum + nums[i] > maxSum) {
        count++;
        sum = 0;
        sum += nums[i];
      } else {
        sum += nums[i];
      }
    }
    return count <= k;
  };

  let left = Math.max(...nums);
  let right = largestSum;
  while (left <= right) {
    let mid = Math.floor((right + left) / 2);
    if (check(mid)) {
      right = mid - 1;
    } else left = mid + 1;
  }

  return left;
};
