def bubbleSort(arr):
    n = len(arr)

    #run the steps n-1 times
    for i in range(n):
        # for each step, max item will come at the last respective index
        for j in range(1, n - i):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
    return arr

print(bubbleSort([3,1,5,4,2]))

        
