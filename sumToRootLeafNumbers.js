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
 * @return {number}
 */
var sumNumbers = function (root) {
  //global answer variable
  //dfs that starts from root and then adds numbers to a string
  //each string gets converted to a number after leaf status confirmed

  let ans = 0;
  let dfs = (node, strng) => {
    if (!node) {
      return 0;
    }
    strng += node.val.toString();
    if (!node.left && !node.right) {
      let completedpath = parseInt(strng);
      ans += completedpath;
    }
    dfs(node.left, strng);
    dfs(node.right, strng);
  };
  dfs(root, "");
  return ans;
};
