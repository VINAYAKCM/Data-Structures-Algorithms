#34. Find first and last position of an element in an sorted array

def searchRange(nums, target):
        ans = [-1 ,-1]
        ans[0] = search(nums, target, True)
        if ans[0] != -1:
            ans[1] = search(nums, target, False)
        return ans

def search(nums, target, findStartIndex):
    ans = -1
    start = 0
    end = len(nums)-1
    while start <= end:
        mid = start + (end - start) // 2
        if target < nums[mid]:
            end = mid - 1
        elif target > nums[mid]:
            start = mid + 1
        else:
            ans = mid
            #check left
            if findStartIndex:
                end = mid - 1
            #check right
            else:
                start = mid + 1
    return ans

print(searchRange([1, 2, 2, 2, 2, 4, 4, 8], 2))