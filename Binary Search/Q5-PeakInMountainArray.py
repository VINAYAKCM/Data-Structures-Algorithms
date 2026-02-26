#Find peak element in an mountain array:

def PeakSearch(arr):
    start = 0
    end = len(arr) - 1

    while start < end:
        mid = start + (end - start) // 2

        if arr[mid] > arr[mid + 1]:
            # you are in descending part of array
            # this may be the answer, but look at left
            # this is why end != mid - 1
            end = mid
        else:
            # you are in ascending part of array
            start = mid + 1  # because we know mid+1 element is greater

    return arr[start]   # or return arr[start] if value needed

# Example usage
arr = [1, 2, 3, 4, 5, 1, 2, 3, 3]
result = PeakSearch(arr)
print(result)