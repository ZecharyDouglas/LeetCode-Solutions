var ladderLength = function (beginWord, endWord, wordList) {
  if (!wordList.includes(beginWord)) {
    wordList.push(beginWord);
  }

  let graph = new Map();
  for (let i = 0; i < wordList.length; i++) {
    graph.set(i, []);
  }

  // Construct the graph
  for (let i = 0; i < wordList.length; i++) {
    for (let j = 0; j < wordList.length; j++) {
      if (i !== j) {
        let dif = 0;
        for (let k = 0; k < beginWord.length; k++) {
          if (wordList[i].charAt(k) !== wordList[j].charAt(k)) dif++;
        }
        if (dif == 1) {
          graph.get(i).push(j);
        }
      }
    }
  }

  let seen = new Array(wordList.length).fill(false);

  let indexBeginWord = wordList.indexOf(beginWord);

  let queue = [wordList.indexOf(beginWord)];

  if (indexBeginWord !== -1) {
    queue = [indexBeginWord];
  } else {
    queue = [beginWord];
  }

  let steps = 1;

  while (queue.length) {
    let nextQueue = [];

    for (let i = 0; i < queue.length; i++) {
      let nodeIndex;
      if (typeof queue[i] === "string") {
        nodeIndex = wordList.indexOf(queue[i]);
      } else {
        nodeIndex = queue[i];
      }

      if (wordList[nodeIndex] === endWord) return steps;
      for (const neighbor of graph.get(nodeIndex)) {
        if (!seen[neighbor]) {
          seen[neighbor] = true;
          nextQueue.push(neighbor);
        }
      }
    }
    queue = nextQueue;
    steps++;
  }
  return 0;
};
