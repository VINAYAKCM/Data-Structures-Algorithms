#Given the array nums after the possible rotation and an integer target, 
#return the index of target if it is in nums, or -1 if it is not in nums.

def RotatedSortedArr(nums, target):
    pivot = nums.index(max(nums))
    firstTry = FirstBS(nums, target, 0, pivot)
    if firstTry != -1:
        return firstTry
    
    return FirstBS(nums, target, pivot + 1, len(nums)-1)

def FirstBS(nums, target, start, end):
    # determine order
    isAsc = nums[start] < nums[end]

    while start <= end:
        mid = start + (end - start) // 2

        if nums[mid] == target:
            return mid

        if isAsc:
            if target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if target > nums[mid]:
                end = mid - 1
            else:
                start = mid + 1

    return -1

nums = [12, 14, 2, 4, 6, 8, 9]
target = 12
print(RotatedSortedArr(nums, target))