var maxVowels = function (s, k) {
  //sliding window
  let maxVowels = 0;
  let vowelCount = 0;
  let left = 0;
  for (let right = 0; right < s.length; right++) {
    if (
      s[right] === "a" ||
      s[right] === "e" ||
      s[right] === "i" ||
      s[right] === "o" ||
      s[right] === "u"
    )
      vowelCount++;
    while (right - left + 1 > k) {
      if (
        s[left] === "a" ||
        s[left] === "e" ||
        s[left] === "i" ||
        s[left] === "o" ||
        s[left] === "u"
      )
        vowelCount--;
      left++;
    }
    maxVowels = Math.max(vowelCount, maxVowels);
  }
  return maxVowels;
};
