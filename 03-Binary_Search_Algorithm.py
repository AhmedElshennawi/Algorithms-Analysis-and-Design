arr_test = [1, 22, 30, 44, 55, 68, 79, 86] # must be sorted

def binary_search(arr, key):
    # key is the object will find by binary_search
    low = 0 
    high = len(arr) - 1
    
    while low <= high:
        mid = (high + low) // 2 
        if key == arr[mid]:
            return mid
        else:
            if key > arr[mid]:
                low = mid + 1 
            else:
                high = mid - 1 
    return -1
    
        
print(binary_search(arr_test, 79))  # 6
print(binary_search(arr_test, 66))  # -1
print(binary_search(arr_test, 0))   # -1
