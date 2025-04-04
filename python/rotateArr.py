
class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self, arr, d):
        n = len(arr)
        d%=n
        
        temp = [0]*n
        
        for i in range(n-d):
            temp[i] = arr[d+i]
            
        for i in range(d):
            temp[n-d+i] = arr[i]
            
        for i in range(n):
            arr[i] = temp[i]
        
        return arr