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
 * @return {number[][]}
 */
var levelOrder = function (root) {
  if (!root) return [];
  let queue = [root];
  let ans = [];
  ans.push([root.val]);
  while (queue.length) {
    let nextQueue = [];
    let nextQueueVals = [];
    for (let i = 0; i < queue.length; i++) {
      if (queue[i].left) {
        nextQueue.push(queue[i].left);
        nextQueueVals.push(queue[i].left.val);
      }
      if (queue[i].right) {
        nextQueue.push(queue[i].right);
        nextQueueVals.push(queue[i].right.val);
      }
    }
    if (nextQueueVals.length) ans.push(nextQueueVals);

    queue = nextQueue;
  }
  return ans;
};
