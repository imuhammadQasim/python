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
// function lengthOfLongestSubstring(str) {
//   let left = 0;
//   let set = new Set();
//   let maxLen = 0;
//   let bestSubstring = "";

//   for (let i = 0; i < str.length; i++) {
//     // shrink window if duplicate found
//     while (set.has(str[i])) {
//       set.delete(str[left]);
//       left++;
//     }

//     // add current character
//     set.add(str[i]);

//     console.log("Set:", set);

//     let windowSize = i - left + 1;
//     console.log("Window size:", windowSize);

//     // update max length (THIS WAS MISSING)
//     // maxLen = Math.max(maxLen, windowSize);
//     if (maxLen < windowSize) {
//       maxLen = windowSize;
//       bestSubstring = str.substring(left, i + 1);
//     }
//   }

//   return {
//     maxLen,
//     bestSubstring,
//   };
// }

// console.log(lengthOfLongestSubstring("pwwkewaw"));
// console.log(lengthOfLongestSubstring("pwwkewaw"));

// function lengthOfLongestSubstring(str) {
//   let left = 0;
//   let maxLen = 0;
//   let substr = "";
//   let set = new Set();

//   for (let i = 0; i < str.length; i++) {
//     while (set.has(str[i])) {
//       set.delete(str[left]);
//       left++;
//     }

//     set.add(str[i]);
//     windowSize = i - left + 1;
//     console.log(set);
//     console.log(windowSize);

//     if (windowSize > maxLen) {
//       maxLen = windowSize;
//       substr = str.substring(left, i + 1);
//     }
//   }

//   return {
//     maxLen,
//     substr,
//   };
// }

// Classic FAANG Logic / Puzzle Questions
// 🎂 1. Cake Cutting (your example)

// Problem:
// You have 1 cake. With 3 straight cuts, what is the maximum number of pieces?

// 👉 Answer idea:

// 3D reasoning in 2D space
// Maximum pieces = 8
// 🔪 2. Pizza Cuts Problem

// Problem:
// What is the maximum number of pieces a pizza can be divided into with n straight cuts?

// 👉 Pattern:

// 1 cut → 2 pieces
// 2 cuts → 4 pieces
// 3 cuts → 7 pieces
// General formula:

// n(n + 1)/2 + 1

// 🪙 3. Coin Flip Puzzle

// Problem:
// You have 100 coins, 10 are heads up. You cannot see them. How do you divide them into 2 groups with equal number of heads?

// 👉 Tests:

// logical grouping
// parity thinking
// 🏢 4. Building Light Switches

// Problem:
// There are 100 light bulbs initially OFF. You toggle them 100 times (1st pass all, 2nd every 2nd, etc). Which bulbs remain ON?

// 👉 Key insight:

// Only perfect squares remain ON
// 🚶 5. Prisoners & Hats

// Problem:
// 100 prisoners in a line, each wearing a black/white hat. They must guess their own hat using only others’ hats.

// 👉 Tests:

// parity encoding strategy
// communication constraints
// 🔢 6. 100 Doors Problem

// Problem:
// 100 doors are toggled in passes (1st all, 2nd every 2nd, etc). Which doors are open?

// 👉 Answer:

// Doors at perfect square positions
// 🎯 7. Water Jug Problem

// Problem:
// You have 3L and 5L jugs. Measure exactly 4L.

// 👉 Tests:

// state space thinking
// BFS-style reasoning
// 🧊 8. Ice Cube Problem (classic estimation)

// Problem:
// How many ice cubes fit in a room?

// 👉 Tests:

// estimation
// dimensional reasoning
// assumptions
// 🧠 9. Ants on a Stick

// Problem:
// Ants move on a stick and collide/reverse direction. When do they fall off?

// 👉 Trick:

// collisions don’t matter (swap identity idea)
// 🎂 10. Cake Sharing (your type)

// Problem variations:

// 2 cuts → max pieces?
// 3 cuts in 3D cake?
// circular cake vs rectangular cake?

// 👉 Tests:

// spatial reasoning
// combinatorics intuition
// 🧠 What FAANG is REALLY testing

// These questions are not about math.

// They test:

// how you reason under ambiguity
// whether you explore edge cases
// whether you find patterns quickly
// whether you simplify complexity
// 🚀 If you want next step

// I can do one of these for you:

// 1. 🔥 Step-by-step solve (like interview simulation)

// I ask you, you respond, I guide

// 2. 🧠 Harder puzzles (Google level)
// missing eggs puzzle
// 12 balls problem
// calendar / probability tricks
// 3. 💻 Convert puzzles into coding problems

// (turn logic puzzles into JS solutions)

// You have 3L and 5L jugs. Measure exactly 4L.

// function fourLiter(3, 5) {
//   if (condition) {

//   }
// }

// num = [2, 1, 7, 11, 15];
// target = 10;
// function two_sum(num, target) {
//   for (let i = 0; i < num.length; i++) {
//     for (let j = 1; j < num.length; j++) {
//       if (num[i] + num[j] == target) {
//         return [i, j];
//       }
//     }
//   }
//   return "N/A";
// }

// console.log(two_sum(num, target));

// function two_sum(num, target) {
//   let map = {};

//   for (let i = 0; i < num.length; i++) {
//     let complement = target - num[i];
//     if (map.hasOwnProperty(complement)) {
//       return [map[complement], i];
//     }

//     map[num[i]] = i;
//   }

//   return "N/A";
// }

// let num = [2, 1, 7, 11, 15];
// let target = 9;

// console.log(two_sum(num, target));

// l = [7, 1, 5, 3, 6, 4];

// function buySell(arr) {
//   minPrice = 100000000;
//   maxProfit = 0;
//   for (let i = 0; i < arr.length; i++) {
//     if (arr[i] < minPrice) {
//       minPrice = arr[i];
//       console.log("IF BLOCK", minPrice);
//     } else {
//       profit = arr[i] - minPrice;
//       console.log("ELSE BLOCK PROFIT", profit);
//       if (maxProfit < profit) {
//         maxProfit = profit;
//       }
//     }
//   }
//   return maxProfit;
// }

// console.log(buySell(l));

// arr = [1, 2, 3, 4, 5, 6, 7, 8, 8, 8, 8, 9];

// function binarySearch(arr, target) {
//   let left = 0;
//   let right = arr.length - 1;

//   while (left <= right) {
//     let mid = Math.floor((left + right) / 2);
//     // console.log(mid);
//     if (arr[mid] === target) {
//       return mid;
//     } else if (arr[mid] > target) {
//       right = mid - 1;
//     } else {
//       left = mid + 1;
//     }
//   }
//   return "Not Found In binary Search";
// }

// console.log(binarySearch(arr, 9));

// function reverseString(str) {
//   reverseStr = "";
//   for (let i = str.length - 1; i >= 0; i--) {
//     reverseStr += str[i];
//   }
//   return reverseStr;
// }

// console.log(reverseString("Hello"));

// let arr = [1, 2, 3, 4, 5, 6, 7, 8, 8, 8, 8, 9];
// function slidingWindow(arr) {
//   let k = 3;
//   let result = [];
//   for (let i = 0; i <= arr.length - k; i++) {
//     result.push(arr.slice(i, i + k));
//   }

//   return result;
// }

// console.log(slidingWindow(arr));

// function two_sum(arr, target) {
//   for (let i = 0; i < arr.length; i++) {
//     for (let j = 0; j < arr.length; j++) {
//       if (arr[j] === arr[i]) {
//         return true;
//       }
//     }
//   }
//   return false;
// }
// console.log(two_sum(arr));
// let arr = [1, 2, 2, 3, 4, 4, 4, 5];
// function two_sum(arr, target) {
//   let map = new Map();
//   for (let i = 0; i < arr.length; i++) {
//     let complement = target - arr[i];
//     console.log("complement:", complement);
//     if (map.has(complement)) {
//       return [map.get(complement), i];
//     }

//     map.set(arr[i], i);
//     console.log(map);
//   }
//   return "Not Found";
// }

// console.log(two_sum(arr, 9));

// let arr = [100, 200, 300, 100];
// function containDuplicates(arr) {
//   let map = new Map();

//   for (let i = 0; i < arr.length; i++) {
//     if (map.has(arr[i])) {
//       return true;
//     } else {
//       map.set(arr[i], i);
//     }
//     console.log(`After ${i} iteration the map is here :`, map);
//   }
//   return false;
// }

// console.log(containDuplicates(arr));

// let a = new Set([3, 4, 5, 6, 0]);
// let b = new Set([1, 2, 3, 4, 5, 6, 7, 8]);

// function symmetricDifference(a, b) {
//   return new Set([
//     ...[...a].filter((x) => !b.has(x)),
//     ...[...b].filter((x) => !a.has(x)),
//   ]);
// }

// console.log(symmetricDifference(a, b));

// let arr = [1, 2, 3, 5, 6, 7];

// function missingNumber(arr) {
//   let currentSum = 0;
//   for (let i = 0; i < arr.length; i++) {
//     currentSum += arr[i];
//   }
//   console.log("current", currentSum);
//   n = Math.max(...arr);
//   console.log(n);
//   actualSum = (n * (n + 1)) / 2;
//   console.log({ actualSum });
//   return actualSum - currentSum;
// }

// console.log(missingNumber(arr));

// nums = [2, 7, 11, 15];
// target = 9;

// function two_sum(nums, target) {
//   let map = new Map();
//   for (let i = 0; i < nums.length; i++) {
//     comp = target - nums[i];
//     console.log(comp);
//     if (map.has(comp)) {
//       return [map.get(comp), i];
//     }

//     map.set(nums[i], i);
//     console.log(map);
//   }
//   return "not FOund";
// }
// console.log(two_sum(nums, target));

// let arr = [1, 2, 2, 3, 4, 4, 4, 5];
// function firstNonRepeating(arr) {
//   let map = new Map();
//   for (let i = 0; i < arr.length; i++) {
//     if (map.has(arr[i])) {
//       map.set(arr[i], map.get(arr[i]) + 1);
//     } else {
//       map.set(arr[i], 1);
//     }
//     console.log(map);
//   }

//   for (let i = 0; i < arr.length; i++) {
//     if (map.get(arr[i]) === 1) {
//       return arr[i];
//     }
//   }
//   return null;
// }

// console.log(firstNonRepeating(arr));

// let arr = [1, 2, 2, 3, 4, 4, 4, 4, 4, 4, 4, 4, 5];
// function majorityRepeating(arr) {
//   let map = new Map();
//   for (let i = 0; i < arr.length; i++) {
//     if (map.has(arr[i])) {
//       map.set(arr[i], map.get(arr[i]) + 1);
//     } else {
//       map.set(arr[i], 1);
//     }
//     console.log(map);
//   }

//   let maxCount = 0;
//   let result = null;

//   for (const [key, value] of map) {
//     if (value > maxCount) {
//       maxCount = value;
//       result = key;
//     }
//   }
//   return [result, maxCount];
// }

// console.log(majorityRepeating(arr));

// let arr = [1, 2, 2, 3, 4, 4, 4, 5];

// function findDuplicates(arr) {
//   let map = new Map();
//   for (let i = 0; i < arr.length; i++) {
//     if (map.has(arr[i])) {
//       map.set(arr[i], map.get(arr[i]) + 1);
//     } else {
//       map.set(arr[i], 1);
//     }
//   }
//   console.log(map);
//   let dupli = [];
//   for (const [key, value] of map) {
//     if (value >= 2) {
//       dupli.push(key);
//     }
//   }
//   return dupli;
// }

// console.log(findDuplicates(arr));

// let nums = [2, 7, 11, 15];
// let target = 13;

// function two_sum(arr, target) {
//   let map = new Map();
//   for (let i = 0; i < arr.length; i++) {
//     const comp = target - arr[i];
//     if (map.has(comp)) {
//       return [map.get(comp), i];
//     }

//     map.set(arr[i], i);
//   }
// }

// console.log(two_sum(nums, target));

// let arr = [1, 2, 3, 4, 5];

// function constainsDuplicate(arr) {
//   let map = new Map();
//   for (let i = 0; i < arr.length; i++) {
//     if (map.has(arr[i])) {
//       return true;
//     }

//     map.set(arr[i], i);
//   }
//   return false;
// }

// console.log(constainsDuplicate(arr));

// function subarraySum(nums, k) {
//   let map = new Map();
//   map.set(0, 1); // important base case

//   let prefixSum = 0;
//   let count = 0;

//   for (let num of nums) {
//     prefixSum += num;

//     let need = prefixSum - k;

//     if (map.has(need)) {
//       count += map.get(need);
//     }

//     map.set(prefixSum, (map.get(prefixSum) || 0) + 1);
//   }

//   return count;
// }

// console.log(subarraySum([1, 2, 3], 3)); // output: 2

// function sumSubArray(arr) {
//   let subArr = [];
//   let k = 3;
//   for (let i = 0; i <= arr.length - k; i++) {
//     let temp = [];
//     for (let j = i; j < k + i; j++) {
//       temp.push(j);
//     }
//     subArr.push(temp);
//   }
//   return subArr;
// }
// var a = [1, 2, 3, 4, 5];
// console.log(sumSubArray(a));

// let a = [1, 2, 3, 4, 5];
// let k = 5;
// function totalSubArrays(arr) {
//   let count = 0;

//   for (let i = 0; i < arr.length; i++) {
//     let temp = [];
//     let sum = 0;
//     for (let j = i; j < arr.length; j++) {
//       temp.push(arr[j]);
//       sum += arr[j];

//       if (sum === k) {
//         count++;
//         console.log("Matched:", temp);
//       }
//     }
//   }

//   return count;
// }

// console.log(totalSubArrays(a));

let a = [23, 2, 4, 6, 7, 3, 3];
let k = 6;
function continouseSubArraySum(arr) {
  for (let i = 0; i < arr.length - 2 + 1; i++) {
    let temp = [];
    let sum = 0;
    for (let j = i; j < arr.length; j++) {
      temp.push(arr[j]);
      sum += arr[j];

      if (sum === k) {
        console.log("Matched:", temp);
      }
    }
  }
}

console.log(continouseSubArraySum(a));
