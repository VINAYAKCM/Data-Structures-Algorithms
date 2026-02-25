#Find ceiling of target in a sorted array
# arr = [1, 2, 8, 10, 10, 12, 19]
# target = 5
# output = 8        

def ceiling(arr, target):
    start = 0
    end = len(arr) - 1

    while start < end:
        mid = start + (end - start)//2
        if target < arr[mid]:
            end = mid - 1
        elif target > arr[mid]:
            start = mid + 1
        else:
            return arr[mid]
        
    return arr[start]

arr = [1, 2, 8, 10, 10, 12, 19]
target = 5

print("Ceil:", ceiling(arr,target))
        
