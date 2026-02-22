def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Example usage
arr = [5, 3, 2, 8, 1]
target = 1
result = linear_search(arr, target)
print("Array position:",result)