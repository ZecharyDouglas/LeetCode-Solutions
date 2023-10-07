//beats only 12% can I make it better?
/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {number[]} restricted
 * @return {number}
 */
var reachableNodes = function (n, edges, restricted) {
  //dfs to travel to the deepest non restricted node and increment a variable for each level of depth
  //max depth variable math.max used to update the variable
  //return the max depth at the end

  let graph = new Map();

  for (let i = 0; i < n; i++) {
    graph.set(i, []);
  }
  for (let i = 0; i < edges.length; i++) {
    graph.get(edges[i][0]).push(edges[i][1]);
    graph.get(edges[i][1]).push(edges[i][0]);
  }
  let maxNodes = 0;
  let seen = new Array(n).fill(false);

  let dfs = (node) => {
    seen[node] = true;
    if (restricted.includes(node)) {
      return;
    }
    maxNodes++;
    for (const neighbor of graph.get(node)) {
      if (!seen[neighbor]) dfs(neighbor);
    }
  };
  dfs(0);
  return maxNodes;
};
