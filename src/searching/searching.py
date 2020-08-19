# python3 src/searching/test_searching.py -v

# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
      
    # Check base case 
    if end >= start: 
        mid = (end + start) // 2
        # If element is present at the middle itself 
        if arr[mid] == target: 
            return mid 
        # If element is smaller than mid, then it can only 
        # be present in left subarray 
        elif arr[mid] > target: 
            return binary_search(arr, target, start, mid - 1) 
        # Else the element can only be present in right subarray 
        else: 
            return binary_search(arr, target, mid + 1, end) 
  
    else: 
        # Element is not present in the array 
        return -1
    


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    start = 0
    end = len(arr) - 1
    first = arr[0]
    last = arr[-1]
    
    if first <= last:
        while end >= start: 
            mid = (end + start) // 2
            if arr[mid] == target: 
                return mid 
            elif arr[mid] > target:
                end = mid -1
            else: 
                start = mid + 1
        else:
            return -1
    else:
        while end >= start: 
            mid = (end + start) // 2
            if arr[mid] == target: 
                return mid
            elif arr[mid] < target:
                end = mid -1
            else:
                start = mid + 1
        else: 
            return -1
