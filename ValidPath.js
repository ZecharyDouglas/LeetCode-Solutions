/* There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, 
where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex source to vertex destination.

Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise. */

/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {number} source
 * @param {number} destination
 * @return {boolean}
 */
var validPath = function (n, edges, source, destination) {
  //convert the 2d array of edges into a graph using a hash map
  //key will be the node and the values will be the edges that node is a part of
  //starting from the source , traverse to a different node via an edge and mark the node as         seen to prevent a cycle
  //use a dfs for the traversal
  //if the node value === destination then return true
  //if all nodes are seen then return false

  //create the graph
  let graph = new Map();
  for (let i = 0; i < n; i++) {
    graph.set(i, []);
  }
  //fill the graph with nodes and array of connected nodes
  for (let edge of edges) {
    graph.get(edge[0]).push(edge[1]);
    graph.get(edge[1]).push(edge[0]);
  }
  //create an array called seen and fill it with false
  let seen = new Array(n).fill(false);

  let ans = false;

  let dfs = (node) => {
    //if node === destination ans = true
    //mark node as seen
    //iterate over node values from hashmap
    //if nodes are not seen then call dfs on their nodes
    if (!seen[node]) {
      if (node === destination) {
        ans = true;
        return ans;
      } else {
        seen[node] = true;
        for (let neighbor of graph.get(node)) {
          //if node isnt seen call dfs on it
          if (!seen[neighbor]) {
            dfs(neighbor);
          }
        }
      }
    }
  };

  //call dfs and return answer
  dfs(source);

  return ans;
};
