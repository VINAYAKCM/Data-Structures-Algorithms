def FindDisappearedNumber(arr):
    i = 0
    while i < len(arr):
        correct = arr[i] - 1
        if arr[i] != arr[correct]:
            arr[i], arr[correct] = arr[correct], arr[i]
        else:
            i += 1
    
    ans = []
    for i in range(len(arr)):
        if arr[i] != i + 1:
            ans.append(i+1)
    
    return ans

print(FindDisappearedNumber([2,3,1,7,8]))