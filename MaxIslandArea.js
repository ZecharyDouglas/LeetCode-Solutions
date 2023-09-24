/**
 * @param {number[][]} grid
 * @return {number}
 */
var maxAreaOfIsland = function (grid) {
  let visited = new Map();
  let maxArea = 0;

  if (!grid || !grid.length || !grid[0].length) return 0;

  let dfs = (i, j) => {
    if (
      i < 0 ||
      i >= grid.length ||
      j < 0 ||
      j >= grid[0].length ||
      visited.has(`${i},${j}`) ||
      grid[i][j] == 0
    ) {
      return 0;
    }

    visited.set(`${i},${j}`, true);

    return 1 + dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1);
  };

  for (let i = 0; i < grid.length; i++) {
    for (let j = 0; j < grid[0].length; j++) {
      if (grid[i][j] == 1 && !visited.has(`${i},${j}`)) {
        maxArea = Math.max(maxArea, dfs(i, j));
      }
    }
  }

  return maxArea;
};
