def push_zeros_to_end(arr):
    non_zero_index = 0

    # Traverse and swap non-zero elements to the front
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i], arr[non_zero_index] = arr[non_zero_index], arr[i]
            non_zero_index += 1
    
    return arr

print(push_zeros_to_end([1, 12, 0, 12, 0, 10, 0]))  # Output: [1, 12, 12, 10, 0, 0, 0]
