/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var threeSumClosest = function (nums, target) {
  //sort nums in ascending order
  //iterate using i in for loop and a left and right pointer to shrink window in while loop
  //compute sum and use Math.abs to update ans with the one that has the lowest abs value difference ( cur vs new calc)
  //return ans

  let ans = nums[0] + nums[1] + nums[nums.length - 1];
  nums.sort((a, b) => a - b);

  for (let i = 0; i < nums.length - 2; i++) {
    let left = i + 1;
    let right = nums.length - 1;

    while (left < right) {
      let sum = nums[i] + nums[left] + nums[right];
      if (sum == target) return sum;
      let check = Math.abs(sum - target);
      let cur = Math.abs(ans - target);

      check < cur ? (ans = sum) : (ans = ans);
      sum > target ? right-- : left++;
    }
  }
  return ans;
};
