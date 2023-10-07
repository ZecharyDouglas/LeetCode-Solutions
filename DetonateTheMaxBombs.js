//beats 66.67 at time of sub
/**
 * @param {number[][]} bombs
 * @return {number}
 */
var maximumDetonation = function (bombs) {
  //if the distance between the points is greater than the max radius of two compared bombs it wont blow
  //convert the bombs array into a graph and map each bomb to another bomb thats in its radius
  //run a dfs that returns the highest num of iterations

  let graph = new Map();

  for (let i = 0; i < bombs.length; i++) {
    graph.set(i, []);
  }

  //filling the graph with mapped connected components
  for (let i = 0; i < bombs.length; i++) {
    for (let j = 0; j < bombs.length; j++) {
      if (i !== j) {
        let bomb = bombs[j];
        //calculate distance
        let distance = Math.sqrt(
          Math.pow(bombs[i][0] - bomb[0], 2) +
            Math.pow(bombs[i][1] - bomb[1], 2)
        );

        //if in range add both ways to graph
        if (distance <= bombs[i][2]) {
          graph.get(i).push(j);
        }
      }
    } //end of inner for loop
  } //end of outer for loop

  let dfs = (node, seen) => {
    if (seen.has(node)) return 0;

    let boom = 1;
    seen.add(node);
    for (const neighbor of graph.get(node)) {
      if (!seen.has(neighbor)) {
        boom += dfs(neighbor, seen);
      }
    }

    return boom;
  };

  let ans = 0;
  for (let i = 0; i < bombs.length; i++) {
    let seen = new Set();
    let result = dfs(i, seen);
    ans = Math.max(ans, result);
  }

  return ans;
};
