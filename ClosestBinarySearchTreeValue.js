/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} target
 * @return {number}
 */

var closestValue = function (root, target) {
  //inorder traversal of the whole tree
  //calculate the absolute value of difference between the target and the node value for each node
  //return the value of the node with the min difference
  let minDif = [Infinity, 0];
  let dfs = (node) => {
    if (node.left) {
      dfs(node.left);
    }

    let temp = Math.abs(target - node.val);
    if (temp < minDif[0]) {
      minDif = [temp, node.val];
    }
    if (node.right) {
      dfs(node.right);
    }
    return minDif[1];
  };
  return dfs(root);
};
