/**
 * @param {string} s
 * @return {string}
 */
var makeGood = function (s) {
  //make a stack out of a string
  //iterate through s and compare top of stack to current iteration
  //if they are opposites pop and skip else push
  //join and return
  let str = [];
  for (let i = 0; i < s.length; i++) {
    if (str.length) {
      let top = str[str.length - 1];
      if (s[i] !== top && s[i].toUpperCase() === top.toUpperCase()) {
        str.pop();
        continue;
      }
    }

    str.push(s[i]);
  }
  return str.join("");
};
