function pushZerosToEnd(arr) {
    let nonZeroIndex = 0;
  
    // Traverse the array and swap non-zero elements to the front
    for (let i = 0; i < arr.length; i++) {
      if (arr[i] !== 0) {
        [arr[i], arr[nonZeroIndex]] = [arr[nonZeroIndex], arr[i]];
        nonZeroIndex++;
      }
    }
  
    return arr;
  }
  
  console.log(pushZerosToEnd([1, 12, 0, 12, 0, 10, 0])); // Output: [1, 12, 12, 10, 0, 0, 0]
  