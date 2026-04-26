// let arr = [2, 3, 0, 5, 6, 6];
// let max = 0;
// for (let I = 0; I < arr.length; I++) {
//   if (max < arr[I]) {
//     max = arr[I];
//   }
// }

// console.log(max);

// arr = [2, 3, 0, 6, 1, 2, 3];
// k = 3;

// let maxArr = [];
// for (let i = 0; i <= arr.length - k; i++) {
//   // let max = arr[i];
//   let temp = [];
//   for (let j = i; j < k + i; j++) {
//     // if (max < arr[j]) {
//     //   max = arr[j];
//     // }
//     temp.push(arr[j]);
//   }
//   maxArr.push(temp);
// }

// console.log(maxArr);

// arr = [2, 1, 5, 1, 3, 2];
// k = 3;
// // let maxSumArr = [];
// let maxSum = 0;
// for (let i = 0; i <= arr.length - k; i++) {
//   sum = 0;
//   for (let j = i; j < k + i; j++) {
//     sum += arr[j];
//   }
//   if (maxSum < sum) {
//     maxSum = sum;
//   }
//   // maxSumArr.push(sum);
// }

// console.log(maxSum);

// function lengthOfLongestSubstring(str) {
//   let set = new Set();
//   let left = 0;
//   let maxLen = 0;

//   for (let right = 0; right < str.length; right++) {
//     // shrink window until valid
//     while (set.has(str[right])) {
//       set.delete(str[left]);
//       left++;
//     }

//     set.add(str[right]);

//     maxLen = Math.max(maxLen, right - left + 1);
//   }

//   return maxLen;
// }

// // Example
// console.log(lengthOfLongestSubstring("pwwkew"));
function lengthOfLongestSubstring(str) {
  let left = 0;
  let set = new Set();
  let maxLen = 0;
  let bestSubstring = "";

  for (let i = 0; i < str.length; i++) {
    // shrink window if duplicate found
    while (set.has(str[i])) {
      set.delete(str[left]);
      left++;
    }

    // add current character
    set.add(str[i]);

    console.log("Set:", set);

    let windowSize = i - left + 1;
    console.log("Window size:", windowSize);

    // update max length (THIS WAS MISSING)
    // maxLen = Math.max(maxLen, windowSize);
    if (maxLen < windowSize) {
      maxLen = windowSize;
      bestSubstring = str.substring(left, i + 1);
    }
  }

  return {
    maxLen,
    bestSubstring,
  };
}

console.log(lengthOfLongestSubstring("pwwkewaw"));
