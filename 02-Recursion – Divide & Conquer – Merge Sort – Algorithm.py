arr_test = [8, 4, 5, 6, 10, 3]


def merge_sort(arr):
    if len(arr) > 1:  # base case
        right_arr = arr[: len(arr)//2]
        left_arr = arr[len(arr)//2 :]
        
        # recursion
        merge_sort(right_arr)
        merge_sort(left_arr)
    
        # merge
        
        i = 0     # index of right arr
        j = 0     # index of left arr
        k = 0     # index of main arr
        
        while i < len(right_arr) and j < len(left_arr):
            if right_arr[i] < left_arr[j]:
                arr[k] = right_arr[i]
                i += 1 
            else:
                arr[k] = left_arr[j]
                j += 1 
            k += 1 
            
        # Copy any remaining elements from right_arr and left_arr  
        while i < len(right_arr):
            arr[k] = right_arr[i]
            i += 1 
            k += 1 
            
        while j < len(left_arr):
            arr[k] = left_arr[j]
            j += 1 
            k += 1 
        
print(arr_test) # [8, 4, 5, 6, 10, 3]
merge_sort(arr_test)
print(arr_test) # [3, 4, 5, 6, 8, 10]
        
