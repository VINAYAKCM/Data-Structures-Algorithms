def search(arr, target, s, e):
    if s > e:                 # base case: not found
        return -1

    m = s + (e - s) // 2      # middle index

    if arr[m] == target:      # target found
        return m

    if target < arr[m]:       # search left half
        return search(arr, target, s, m - 1)

    return search(arr, target, m + 1, e)   # search right half


# main equivalent
arr = [1, 2, 3, 4, 55, 66, 78]
target = 4

print(search(arr, target, 0, len(arr) - 1))