var isSameTree = function (p, q) {
  //dfs that takes a node from each of the trees at a given step and then compares their existance and values
  let dfs = (a, b) => {
    if (a === null && b === null) return true;

    if (a === null && b !== null) return false;

    if (b === null && a !== null) return false;

    if (a.val !== b.val) return false;

    return dfs(a.left, b.left) && dfs(a.right, b.right);
  };

  return dfs(p, q);
};
