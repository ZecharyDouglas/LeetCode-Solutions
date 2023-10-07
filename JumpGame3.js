//Beats 44.29% of JS subs at time of sub
/**
 * @param {number[]} arr
 * @param {number} start
 * @return {boolean}
 */
var canReach = function (arr, start) {
  if (arr[start] == 0) return true;

  let queue = [start];

  //node here needs to be an index
  let jumper = (node) => {
    let ans = [];
    ans.push(arr[node] + node);
    ans.push(node - arr[node]);
    return ans;
  };

  let seen = new Set();

  while (queue.length) {
    let nextQueue = [];

    for (let i = 0; i < queue.length; i++) {
      let node = queue[i];
      if (arr[node] === 0) return true;
      for (const jump of jumper(node)) {
        if (!seen.has(jump) && jump >= 0) {
          seen.add(jump);
          nextQueue.push(jump);
        }
      }
      queue = nextQueue;
    }
  }

  return false;
};
