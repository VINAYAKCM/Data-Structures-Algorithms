def search(arr, target):
    peak = peakIndexInMountainArray(arr)

    # try searching in ascending part
    first_try = orderAgnosticBS(arr, target, 0, peak)
    if first_try != -1:
        return first_try

    # search in descending part
    return orderAgnosticBS(arr, target, peak + 1, len(arr) - 1)


def peakIndexInMountainArray(arr):
    start = 0
    end = len(arr) - 1

    while start < end:
        mid = start + (end - start) // 2

        if arr[mid] > arr[mid + 1]:
            # descending part
            end = mid
        else:
            # ascending part
            start = mid + 1

    return start


def orderAgnosticBS(arr, target, start, end):
    # determine order
    isAsc = arr[start] < arr[end]

    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid] == target:
            return mid

        if isAsc:
            if target < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if target > arr[mid]:
                end = mid - 1
            else:
                start = mid + 1

    return -1

arr = [1,2,3,4,5,3,1]
target = 3
print(search(arr, target))