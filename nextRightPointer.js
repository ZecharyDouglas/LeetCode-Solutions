var connect = function (root) {
  //bfs traversal
  //nodes in queue have their .next set to the next node in the level
  //the node at the end in the current level has its .next set to null
  if (!root) return null;

  let queue = [root];
  while (queue.length) {
    let nextqueue = [];

    for (let i = 0; i < queue.length; i++) {
      let node = queue[i];

      if (node.left) {
        nextqueue.push(node.left);
      }
      if (node.right) {
        nextqueue.push(node.right);
      }
    }
    for (let i = 0; i < nextqueue.length - 1; i++) {
      nextqueue[i].next = nextqueue[i + 1];
    }
    queue = nextqueue;
  }
  return root;
};
