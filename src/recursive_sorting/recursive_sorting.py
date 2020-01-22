def merge(arrA, arrB):
    # Get length of end array
    elements = len(arrA) + len(arrB)
    # Create empty array to be filled
    merged_arr = [0] * elements
    # counter of index to insert at
    cur_index = 0
    # as long as both arrays still have elements
    while len(arrA) > 0 and len(arrB) > 0:
        # compare the first elements, and put the smaller in the merged array
        if arrA[0] < arrB[0]:
            merged_arr[cur_index] = arrA.pop(0)
            cur_index += 1
        else:
            merged_arr[cur_index] = arrB.pop(0)
            cur_index += 1

    # when one array runs out of elements
    # find the array thats not empty
    # one at a time, insert into merged array
    if len(arrA) == 0:
        for num in arrB:
            merged_arr[cur_index] = num
            cur_index += 1
    elif len(arrB) == 0:
        for num in arrA:
            merged_arr[cur_index] = num
            cur_index += 1
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    # base case, array len 0 or 1
    if len(arr) < 2:
        return arr
    # split array in half
    else:
        mid = len(arr) // 2
        first = arr[:mid]
        second = arr[mid:]
    # implement recursion to split until base case
    first = merge_sort(first)
    second = merge_sort(second)
    # merge em back up
    arr = merge(first, second)
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
