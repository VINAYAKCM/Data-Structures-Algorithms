#Find an element in an Infinite Array(no bounds, no start, no end)

def InfiniteSearch(arr, target):
    start = 0
    end = 1

    while target > arr[end]:
        new_start = end + 1
        window_size = end - start + 1
        end = end + window_size * 2
        start = new_start

    return binarySearch(arr, target, start, end)


def binarySearch(arr, target, start, end):
    while start <= end:
        mid = start + (end - start) // 2

        if target < arr[mid]:
            end = mid - 1
        elif target > arr[mid]:
            start = mid + 1
        else:
            return mid

    return -1

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5
print(InfiniteSearch(arr, target))