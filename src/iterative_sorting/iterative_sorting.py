# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # for every num in arr:
    for i in range(0, len(arr)-1):
        # look for smallest number by:
        # storing the number were up to
        smallest_index = i
        smallest_num = arr[i]
        # loop through rest of list:
        for num in arr[i+1:]:
            # replace if we find something smaller
            if num < smallest_num:
                smallest_num = num
                smallest_index = arr.index(num)
        # swap smallest number with current spot
        temp = arr[i]
        arr[i] = smallest_num
        arr[smallest_index] = temp
    # return sorted list
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # look at all neighbor combos in arr
    print(arr)
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            print(arr[j], arr[j+1])
            if arr[j] > arr[i+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
