def FindAllDuplicates(arr):
    i = 0
    # cyclic sort
    while i < len(arr):
        correct = arr[i] - 1
        if arr[i] != arr[correct]:
            arr[i], arr[correct] = arr[correct], arr[i]  # place number correctly
        else:
            i += 1
    ans = []
    # find numbers not at correct index
    for i in range(len(arr)):
        #if value doesnt match its position:
        if arr[i] != i + 1:
            ans.append(arr[i])   # duplicate number
    return ans

print(FindAllDuplicates([4,3,2,7,8,2,3,1]))