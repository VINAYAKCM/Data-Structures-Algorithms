def InsertionSort(arr):
    # iterate over array starting from index 0 to second last element
    for i in range(len(arr)-1):
        # start from the element after i, stop at 0th index while parsing back and move backwards by -1 increment
        for j in range(i+1, 0, -1):
            if arr[j] < arr[j -1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                # stop early because the element is already in correct position beacuse all the elements before it are already sorted
                break
    return arr

print(InsertionSort([3,5,4,1,2]))

