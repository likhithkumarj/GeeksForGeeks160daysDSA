class Solution:
    # Function returns the second largest element
    def getSecondLargest(self, arr):
        if len(arr) < 2:
            return -1
        
        largest = second_largest = float('-inf')
        
        for num in arr:
            if num > largest:
                second_largest = largest
                largest = num
            elif num > second_largest and num != largest:
                second_largest = num
        
        return -1 if second_largest == float('-inf') else second_largest

# Example usage
solution = Solution()
print(solution.getSecondLargest([12, 35, 1, 10, 34, 1]))  # Output: 34
print(solution.getSecondLargest([10, 5, 10]))            # Output: 5
print(solution.getSecondLargest([10, 10, 10]))           # Output: -1