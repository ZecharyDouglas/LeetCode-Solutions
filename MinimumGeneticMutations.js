//beats 85.76% of js submissions at time of submission

/**
 * @param {string} startGene
 * @param {string} endGene
 * @param {string[]} bank
 * @return {number}
 */
var minMutation = function (startGene, endGene, bank) {
  if (!bank.includes(endGene)) {
    return -1;
  }

  if (startGene == endGene) return 0;

  let mutations = (node) => {
    let ans = [];
    for (let i = 0; i < 8; i++) {
      for (const change of ["A", "T", "G", "C"]) {
        if (node[i] !== change) {
          //slice until the ith position add the change and slice after i+1 , then concat string
          let back = node.slice(0, i);
          let front = node.slice(i + 1);
          let newMutation = back + change + front;
          ans.push(newMutation);
        }
      }
    }
    return ans;
  };

  let queue = [startGene];
  let seen = new Set();
  seen.add(startGene);
  let steps = 0;

  while (queue.length) {
    let nextQueue = [];
    for (let i = 0; i < queue.length; i++) {
      let node = queue[i];
      if (node === endGene) return steps;
      for (const mutation of mutations(node)) {
        if (!seen.has(mutation) && bank.includes(mutation)) {
          seen.add(mutation);
          nextQueue.push(mutation);
        }
      }
    }
    queue = nextQueue;
    steps++;
  }

  return -1;
};
