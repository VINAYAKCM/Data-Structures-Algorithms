def quick_sort(arr):

    # base case
    if len(arr) <= 1:
        return arr

    pivot = arr[0]

    left = []
    right = []

    for x in arr[1:]:
        if x <= pivot:
            left.append(x)
        else:
            right.append(x)

    return quick_sort(left) + [pivot] + quick_sort(right)


arr = [5,3,8,4,2,7,1]
print(quick_sort(arr))