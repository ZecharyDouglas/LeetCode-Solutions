/**
 * @param {number[][]} graph
 * @return {number[][]}
 */
var allPathsSourceTarget = function (graph) {
  //add all the nodes and their neighbors to a graph
  //back tracking function
  //keep track of nodes visited using curr
  //push to curr (array)
  //add curr to answer array when the target node is visited
  let map = new Map();
  let ans = [];
  for (let i = 0; i < graph.length; i++) {
    if (!map.has(i)) {
      map.set(i, []);
    }
    for (let j = 0; j < graph[i].length; j++) {
      map.get(i).push(graph[i][j]);
    }
  }
  let backtrack = (curr, node) => {
    if (node == graph.length - 1) {
      ans.push([...curr]);
      return;
    }
    curr.push(node);
    for (const neighbor of map.get(node)) {
      backtrack(curr, neighbor);
      curr.pop();
    }
  };
  backtrack([], 0);
  return ans;
};
