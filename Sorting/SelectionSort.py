def selectionSort(arr):
    n = len(arr)

    for i in range(n):
        last = n - i - 1
        maxIndex = 0

        # find max index in arr[0:last]
        for j in range(1, last + 1):
            if arr[j] > arr[maxIndex]:
                maxIndex = j

        # swap
        arr[maxIndex], arr[last] = arr[last], arr[maxIndex]

    return arr

print(selectionSort([3,2,1,5,4]))