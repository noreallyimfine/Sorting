# STRETCH: implement Linear Search
def linear_search(arr, target):
    # TO-DO: add missing code
    for num in arr:
        if num == target:
            return arr.index(num)
    return -1   # not found


# STRETCH: write an iterative implementation of Binary Search
def binary_search(arr, target):

    if len(arr) == 0:
        return -1  # array empty

    low = 0
    high = len(arr)-1

    # TO-DO: add missing code
    while high - low > 0:
        mid = (high - low) // 2
        item = arr[mid]
        if item == target:
            return True
        elif item > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1  # not found


# STRETCH: write a recursive implementation of Binary Search
def binary_search_recursive(arr, target):
    middle = len(arr) // 2

    if len(arr) == 0:
        return -1  # array empty
    # TO-DO: add missing if/else statements, recursive calls
    if middle == target:
        return True
    elif middle > target:
        return binary_search_recursive(arr[:middle-1], target)
    else:
        return binary_search_recursive(arr[middle+1:], target)

