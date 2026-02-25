def binarySearch(arr, target):
    start = 0
    end = len(arr) - 1

    while start <= end:
        # find the middle element
        mid = start + (end - start) // 2

        if target < arr[mid]:
            end = mid - 1
        elif target > arr[mid]:
            start = mid + 1
        else:
            # ans found
            return mid

    return -1

# Example usage
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5
result = binarySearch(arr, target)
print(result)