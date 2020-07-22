# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements
    arrA_index, arrB_index = 0, 0
    merged_arr = []
    while arrA_index < len(arrA) and arrB_index < len(arrB):
        if arrA[arrA_index] < arrB[arrB_index]:
            merged_arr.append(arrA[arrA_index])
            arrA_index += 1
        else:
            merged_arr.append(arrB[arrB_index])
            arrB_index += 1

    merged_arr += arrA[arrA_index:]
    merged_arr += arrB[arrB_index:]

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) <= 1:  # base case
        return arr

    # divide array in half and merge sort recursively
    half = len(arr) // 2
    arrA = merge_sort(arr[:half])
    arrB = merge_sort(arr[half:])

    arr = merge(arrA, arrB)
    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    return
    # Your code here


def merge_sort_in_place(arr, l, r):
    return
    # Your code here

