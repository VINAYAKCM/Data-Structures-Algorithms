def merge_sort(arr):
    
    # base case
    if len(arr) <= 1:
        return arr

    # divide
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # merge
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    # compare elements
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # remaining elements
    result.extend(left[i:])
    result.extend(right[j:])

    return result


arr = [5,3,8,4,2,7,1]
print(merge_sort(arr))