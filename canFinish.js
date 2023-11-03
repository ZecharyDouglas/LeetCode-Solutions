var canFinish = function (numCourses, prerequisites) {
  let graph = new Map();
  for (let i = 0; i < prerequisites.length; i++) {
    if (!graph.has(prerequisites[i][1])) {
      // Check if graph has the key
      graph.set(prerequisites[i][1], []);
    }
    graph.get(prerequisites[i][1]).push(prerequisites[i][0]);
  }

  let dfs = (node, seen) => {
    if (seen[node]) return false; // If already seen, a cycle is detected
    if (!graph.has(node)) return true; // No more prerequisites, course can be finished

    seen[node] = true;
    for (const neighbor of graph.get(node) || []) {
      // Ensure the array is iterable
      if (!dfs(neighbor, seen)) return false;
    }
    seen[node] = false; // Backtrack and mark the node as unseen for other paths
    graph.set(node, []); // Mark the node as fully explored
    return true;
  };

  for (let i = 0; i < numCourses; i++) {
    let seen = new Array(numCourses).fill(false);
    if (!dfs(i, seen)) return false; // If a cycle is detected, return false
  }

  return true; // If all courses can be taken without cycles, return true
};
