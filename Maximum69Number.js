/**
 * @param {number} num
 * @return {number}
 */
var maximum69Number = function (num) {
  //convert the num into a string , and iterate through each char
  //if the element is equal to 9 go to the next character in sequence else flip and return as a number
  let str = num.toString().split("");

  for (let c = 0; c < str.length; c++) {
    if (str[c] === "6") {
      str[c] = "9";
      return Number(str.join(""));
    } else {
      continue;
    }
  }
  return str.join("");
};
