var largestAltitude = function (gain) {
  //prefix sum that first starts with 0
  //max altitude variable that is the math.max of the altitude through all iterations
  let maxAlt = 0;
  let altitudes = [];
  altitudes.push(0);
  for (let i of gain) {
    altitudes[0] += i;
    maxAlt = Math.max(maxAlt, altitudes[0]);
  }
  return maxAlt;
};
