def binary_search(arr, target):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = start + (end - start)//2
        if target < arr[mid]:
            end = mid - 1
        elif target > arr[mid]:
            start = mid + 1
        else:
            return mid
    return -1

# Example usage
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5
result = binary_search(arr, target)
print(result)