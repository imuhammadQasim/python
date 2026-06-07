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
// let a = [1, 2, 3, 4]; // Length: 4 (Longer)
// let b = [9, 10];
// function merge(a, b) {
//   let left = 0;
//   let right = 0;
//   let result = [];

//   while (left < a.length && right < b.length) {
//     if (a[left] > b[right]) {
//       result.push(b[right]);
//       right++;
//     } else {
//       result.push(a[left]);
//       left++;
//     }
//   }

//   while (left < a.length) {
//     result.push(a[left]);
//     left++;
//   }
//   while (right < b.length) {
//     result.push(b[right]);
//     right++;
//   }

//   return result;
// }

// function mergeSort(arr) {
//   if (arr.length <= 1) {
//     return arr;
//   }

//   let mid = Math.floor(arr.length / 2);

//   let leftHalf = arr.slice(0, mid);
//   let rightHalf = arr.slice(mid);

//   return merge(mergeSort(leftHalf), mergeSort(rightHalf));
// }

// let unsortedArray = [34, 7, 23, 32, 5, 62];
// console.log(mergeSort(unsortedArray));

// class Box {
//   constructor(toy) {
//     this.toy = toy; // The item inside the box
//     this.next = null; // The note pointing to the next box (starts blank)
//   }
// }

// // Let's create three separate boxes
// let boxA = new Box("Teddy Bear");
// let boxB = new Box("Toy Car");
// let boxC = new Box("Robot");
// boxA.next = boxB;
// boxB.next = boxC;

// let head = boxA;
// console.log(head);
// let currentBox = head;
// while (currentBox !== null) {
//   console.log("Found: " + currentBox.toy);

//   currentBox = currentBox.next;
// }

// class Node {
//   constructor(data) {
//     this.data = data;
//     this.next = null;
//   }
// }

// class LinkededList {
//   constructor() {
//     this.head = null;
//   }

//   append(data) {
//     const newNode = new Node(data);
//     if (this.head === null) {
//       this.head = newNode;
//       return;
//     }

//     let current = this.head;
//     while (current.next !== null) {
//       current = current.next;
//     }
//     current.next = newNode;
//   }

//   printList() {
//     let current = this.head;

//     let result = "";
//     while (current !== null) {
//       result += current.data + " => ";
//       current = current.next;
//     }
//     console.log(result + "null ");
//   }
// }

// const myList = new LinkededList();

// myList.append(10);
// myList.append(20);
// myList.append(40);
// myList.printList();

// class Node {
//   constructor(data) {
//     this.data = data;
//     this.next = null;
//   }
// }
// class LinkedList {
//   constructor() {
//     this.head = null;
//   }

//   append(data) {
//     const newNode = new Node(data);
//     if (this.head === null) {
//       this.head = newNode;
//       return;
//     }

//     let current = this.head;
//     while (current.next !== null) {
//       current = current.next;
//     }

//     current.next = newNode;
//     // console.log(this.head);
//   }

//   printList() {
//     let current = this.head;
//     let result = "";
//     while (current !== null) {
//       result += current.data + " => ";
//       current = current.next;
//     }
//     console.log(result + "null ");
//   }
// }

// const myList = new LinkedList();

// myList.append(10);
// myList.append(20);
// myList.append(30);
// myList.append(40);
// myList.printList();

// 1. The Bidirectional Building Block
// class Node {
//   constructor(data) {
//     this.data = data;
//     this.next = null; // Points to the next node
//     this.prev = null; // Points to the previous node 👈 NEW
//   }
// }

// // 2. The Management Wrapper
// class DoublyLinkedList {
//   constructor() {
//     this.head = null;
//     this.tail = null; // Tracks the end for easy reverse traversal 👈 NEW
//   }

//   // Add a node to the end
//   append(data) {
//     const newNode = new Node(data);

//     // Case 1: The list is empty
//     if (this.head === null) {
//       this.head = newNode;
//       this.tail = newNode; // Head and Tail are the same node
//       return;
//     }

//     // Case 2: The list has items
//     // No while loop needed! We can jump straight to the tail.
//     this.tail.next = newNode; // Old tail points forward to new node
//     newNode.prev = this.tail; // New node points backward to old tail 👈 NEW
//     this.tail = newNode; // Move the tail marker to the new node
//   }

//   // Print forward from Head to Tail
//   printForward() {
//     let current = this.head;
//     let result = "Forward: ";
//     while (current !== null) {
//       result += current.data + " <-> ";
//       current = current.next;
//     }
//     console.log(result + "null");
//   }

//   // Print backward from Tail to Head 👈 NEW
//   printBackward() {
//     let current = this.tail; // Start at the end
//     let result = "Backward: null";
//     while (current !== null) {
//       result = result + " <-> " + current.data; // Build string backwards
//       current = current.prev; // Move backward using prev pointer
//     }
//     console.log(result);
//   }
// }

// // --- Usage ---
// const myDLL = new DoublyLinkedList();
// myDLL.append(10);
// myDLL.append(20);
// myDLL.append(30);

// myDLL.printForward(); // Output: Forward: 10 <-> 20 <-> 30 <-> null
// myDLL.printBackward(); // Output: Backward: null <-> 10 <-> 20 <-> 30

let arr = [1, 2, 3, 4, 5, 6, 7, 8];
let k = 3;

function listed(arr, k) {
  let maxSum = Infinity;
  for (let i = 0; i < arr.length - k + 1; i++) {
    let sum = 0;
    for (let j = i; j < k + i; j++) {
      sum += arr[j];
    }
    console.log(`maxSum in ${i} iteration is ${maxSum}`);
    if (sum < maxSum) {
      maxSum = sum;
    }
  }
  console.log(maxSum);
}

listed(arr, k);
