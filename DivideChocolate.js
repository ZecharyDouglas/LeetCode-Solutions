/**
 * @param {number[]} sweetness
 * @param {number} k
 * @return {number}
 */
var maximizeSweetness = function (sweetness, k) {
  let check = (sugar) => {
    let sum = 0;
    let pieces = 0;
    for (let i = 0; i < sweetness.length; i++) {
      sum += sweetness[i];
      if (sum >= sugar) {
        sum = 0;
        pieces++;
      }
    }
    return pieces >= k + 1;
  };
  let low = 1;
  let high = sweetness.reduce((acc, num) => (acc += num), 0) / (k + 1);
  while (low <= high) {
    let mid = Math.ceil((high + low) / 2);
    if (check(mid)) {
      low = mid + 1;
    } else {
      high = mid - 1;
    }
  }
  return high;
};
