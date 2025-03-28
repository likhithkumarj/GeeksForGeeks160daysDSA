class Solution {
    // Function returns the second largest element
    getSecondLargest(arr) {
        if (arr.length < 2) return -1;

        let largest = -Infinity;
        let secondLargest = -Infinity;

        for (let num of arr) {
            if (num > largest) {
                secondLargest = largest;
                largest = num;
            } else if (num > secondLargest && num !== largest) {
                secondLargest = num;
            }
        }

        return secondLargest === -Infinity ? -1 : secondLargest;
    }
}

// Example usage:
const solution = new Solution();
console.log(solution.getSecondLargest([12, 35, 1, 10, 34, 1])); // Output: 34
console.log(solution.getSecondLargest([10, 5, 10]));            // Output: 5
console.log(solution.getSecondLargest([10, 10, 10]));           // Output: -1
