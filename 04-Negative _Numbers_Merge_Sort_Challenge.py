arr_test = [-1, 2, -3, 4, -6, 7]

def merge_sort(arr):
    if len(arr) > 1:
        left_arr = arr[len(arr) // 2 :]
        right_arr = arr[: len(arr) // 2]
        
        merge_sort(left_arr)
        merge_sort(right_arr)
        
        i = 0 
        j = 0 
        k = 0 
        
        while i < len(left_arr) and left_arr[i] < 0:
            arr[k] = left_arr[i]
            i += 1 
            k += 1 
        while j < len(right_arr) and right_arr[j] < 0:
            arr[k] = right_arr[j]
            j += 1 
            k += 1 
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1 
            k += 1 
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1 
            k += 1 

# Test the code
print("Original array:", arr_test) # Original array: [-1, 2, -3, 4, -6, 7]
merge_sort(arr_test)
print("Sorted array with negative numbers first:", arr_test) # Sorted array with negative numbers first: [-6, -3, -1, 7, 4, 2]
