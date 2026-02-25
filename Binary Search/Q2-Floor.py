#Find floor of target in a sorted array
# arr = [1, 2, 8, 10, 10, 12, 19]
# target = 5
# output = 2

def floor(arr, target):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = start + (end - start)//2
        if arr[mid] == target:
            return arr[mid]
        elif arr[mid] < target:
            start = mid + 1   # move right
        else:
            end = mid - 1     # move left
    
    return arr[end]

arr = arr = [1, 2, 8, 10, 10, 12, 19]
target = 5
print("Floor:", floor(arr, target))