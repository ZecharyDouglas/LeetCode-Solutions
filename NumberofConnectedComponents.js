/**
 * @param {number} n
 * @param {number[][]} edges
 * @return {number}
 */
var countComponents = function (n, edges) {
  //create a graph to convert the 2d array via hashmap
  //fill the graph by iteration through the array
  //create a seen array and fill with false
  //loop to iterate through the nodes marking node as seen and call dfs on node to iterate connected nodes
  //ans incremented in loop if node is not seen
  //return answer

  let graph = new Map();

  for (let i = 0; i < n; i++) {
    graph.set(i, []);
  }

  for (let i = 0; i < edges.length; i++) {
    graph.get(edges[i][0]).push(edges[i][1]);
    graph.get(edges[i][1]).push(edges[i][0]);
  }
  let seen = new Array(n).fill(false);

  let ans = 0;
  let dfs = (node) => {
    seen[node] = true;
    for (const neighbor of graph.get(node)) {
      if (!seen[neighbor]) {
        dfs(neighbor);
      }
    }
  };

  for (let i = 0; i < n; i++) {
    if (!seen[i]) {
      ans++;
      dfs(i);
    }
  }
  return ans;
};
