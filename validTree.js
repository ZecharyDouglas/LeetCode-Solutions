/**
 * @param {number} n
 * @param {number[][]} edges
 * @return {boolean}
 */
var validTree = function (n, edges) {
  //add nodes to a map
  //perform a dfs traversal through the nodes
  //seen array so nodes can be either visited , or unvisited
  //unvisited = 0 , visited = 1
  //check for seen nodes that are not parents of the current nodes , if the neighbor is seen and its not the parent then it is a cycle
  if (edges.length != n - 1) return false;

  let map = new Map();
  let nodesTracker = new Array(n).fill(0);

  for (const node of edges) {
    let [a, b] = node;
    if (!map.has(a)) {
      map.set(a, []);
    }
    if (!map.has(b)) {
      map.set(b, []);
    }
    map.get(a).push(b);
    map.get(b).push(a);
  }

  let stack = [[0, -1]];
  nodesTracker[0] = 1;

  while (stack.length) {
    let [node, parent] = stack.pop();
    for (const neighbor of map.get(node) || []) {
      if (nodesTracker[neighbor] == 0) {
        nodesTracker[neighbor] = 1;
        stack.push([neighbor, node]);
      } else if (parent !== neighbor) {
        return false;
      }
    }
  }

  return nodesTracker.every((status) => status == 1);
};
