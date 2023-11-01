/**
 * @param {number} n
 * @param {number[][]} roads
 * @return {number}
 */
var maximalNetworkRank = function (n, roads) {
  //find the cities via an adjacency list with the highest numbers of nodes
  //add connections into a graph
  //iterate through the cities and the sizes of their sets , representing connections and update the max
  //return the max
  let graph = new Map();

  for (let i = 0; i < roads.length; i++) {
    if (!graph.has(roads[i][0])) {
      graph.set(roads[i][0], new Set());
    }
    graph.get(roads[i][0]).add(roads[i][1]);

    if (!graph.has(roads[i][1])) {
      graph.set(roads[i][1], new Set());
    }
    graph.get(roads[i][1]).add(roads[i][0]);
  }
  let maxRank = 0;
  for (let i = 0; i < n; i++) {
    for (let j = i + 1; j < n; j++) {
      let sum =
        (graph.get(i) ? graph.get(i).size : 0) +
        (graph.get(j) ? graph.get(j).size : 0);
      if (graph.get(i) && graph.get(i).has(j)) {
        sum -= 1;
      }
      maxRank = Math.max(maxRank, sum);
    }
  }

  return maxRank;
};
