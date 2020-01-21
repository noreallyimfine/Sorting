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
            return mid
        elif item > target:
            high = mid
        else:
            low = mid
    return -1  # not found


# STRETCH: write a recursive implementation of Binary Search
def binary_search_recursive(arr, target, low, high):
    if len(arr) == 0:
        return -1  # array empty
    # TO-DO: add missing if/else statements, recursive calls
    middle = (high - low) // 2
    item = arr[middle]
    if item == target:
        return middle
    elif item > target:
        high = middle
        return binary_search_recursive(arr[:high], target, low, high)
    else:
        low = middle
        return binary_search_recursive(arr[low:], target, low, high)
