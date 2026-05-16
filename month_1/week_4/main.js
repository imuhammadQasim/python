// let a = [1, 2, 3, 4, 6];
// let target = 6;

// function pair_sum(arr, target) {
//   let left = 0;
//   let right = arr.length - 1;

//   while (left < right) {
//     let sum = arr[left] + arr[right];
//     console.log(sum);
//     if (sum === target) {
//       return [left, right];
//     } else if (sum < target) {
//       left++;
//     } else {
//       right--;
//     }
//   }

//   return "not found";
// }

// console.log(pair_sum(a, target));

// let a = [1, 2, 3, 4, 5, 6];

// function reverseInLine(arr) {
//   let left = 0;
//   let right = arr.length - 1;

//   while (left < right) {
//     let temp = arr[left];
//     arr[left] = arr[right];
//     arr[right] = temp;

//     left++;
//     right--;
//   }
//   return arr;
// }

// console.log(reverseInLine(a));

// let string = "holoh";

// function checkPalindrome(str) {
//   let left = 0;
//   let right = str.length - 1;

//   while (left <= right) {
//     if (str[left] !== str[right]) {
//       return "Not Palindrome";
//     }
//     left++;
//     right--;
//   }
//   return "String is Plaindome";
// }

// console.log(checkPalindrome(string));

// let a = [0, 1, 2, 0, 3, 1, 0];

// function removeDuplicate(arr) {
//   let i = 0;
//   for (let j = 1; j < arr.length; j++) {
//     if (arr[j] !== arr[i]) {
//       temp = arr[i];
//       i++;
//       arr[i] = arr[j];
//       arr[j] = temp;
//     }
//   }
//   console.log(i);
//   return arr;
// }

// console.log(removeDuplicate(a));

// let a = [0, 1, 2, 0, 3, 1, 0];

// function moveZero(arr) {
//   let k = 0;
//   for (let i = 0; i < arr.length; i++) {
//     if (arr[i] !== 0) {
//       console.log(arr[i]);
//       arr[k] = arr[i];
//       k++;
//     }
//   }
//   for (let j = k; j < arr.length; j++) {
//     arr[j] = 0;
//   }
//   return arr;
// }

// console.log(moveZero(a));

// let a = [1, 2, 3, 4, 3, 3, 6];

// function removeElement(arr, val) {
//   let i = 0;
//   for (let j = 0; j < arr.length; j++) {
//     if (arr[j] !== val) {
//       arr[i] = arr[j];
//       i++;
//     }
//   }
//   return arr.slice(0, i);
// }

// console.log(removeElement(a, 3));

// let a = [-4, -1, 0, 3, 10];

// function sortedSqaures(arr) {
//   let i = 0;
//   for (let j = arr.length - 1; j >= 0; j--) {
//     iSqaure = arr[i] ** 2;
//     jSqaure = arr[j] ** 2;
//     console.log(iSqaure);
//     if (iSqaure > jSqaure) {
//       let temp = iSqaure;
//       arr[i] = jSqaure;
//       arr[j] = temp;
//     }
//     i++;
//   }
//   return arr;
// }

// console.log(sortedSqaures(a));

// function pattern(rows) {
//   for (let i = 1; i <= rows; i++) {
//     let line = "";

//     for (let s = 0; s < rows - i; s++) {
//       line += " ";
//     }

//     for (let j = 1; j <= i; j++) {
//       line += j;
//     }
//     console.log(line);
//   }
// }

// pattern(5);

// function fun(n) {
//   debugger; // Execution pauses here

//   if (n > 0) {
//     return fun(n - 1) + n;
//   }
//   return 0;
// }

// fun(3);

let a = [1, 4, 6, 7];
let b = [2, 3, 5, 9, 10];

function merge(a, b) {
  let left = 0;
  let right = 0;
  let result = [];

  while (left < a.length && right < b.length) {
    if (a[left] > b[right]) {
      result.push(b[right]);
      right++;
    } else {
      result.push(a[left]);
      left++;
    }
  }

  while (left < a.length) {
    result.push(a[left]);
    left++;
  }
  while (right < b.length) {
    result.push(b[right]);
    right++;
  }

  return result;
}

console.log(merge(a, b));
