var reverse = function (x) {
  // iterations of division by a divisor answer gets unshifted into answer array
  // return Number(array.join(""))
  let sign;
  x < 0 ? (sign = -1) : (sign = 1);

  let num = Math.abs(x);
  let ans = [];
  if (x == 0) return 0;
  let divisor = 1;
  while (num / divisor >= 10) {
    divisor *= 10;
  }

  while (num > 0) {
    let leadingDigit = Math.floor(num / divisor);
    ans.unshift(leadingDigit);
    num %= divisor;
    divisor /= 10;
  }

  let reversed = parseInt(ans.join("")) * sign;
  if (reversed > Math.pow(2, 31) - 1 || reversed < Math.pow(-2, 31) - 1)
    return 0;
  return reversed;
};
