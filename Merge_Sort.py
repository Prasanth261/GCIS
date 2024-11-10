arr=[1,123,53,13,643,13,5,1,3]

def merge_sort(arr):
    if len(arr) > 1:
        ratio = 0.5  # 70-30 split
        split_index = int(len(arr) * ratio)
        left_arr = arr[:split_index]
        right_arr = arr[split_index:]
        merge_sort(left_arr)
        merge_sort(right_arr)
        
        i = 0  # left array index
        j = 0  # right array index
        k = 0  # merged array index
        
        # Compare and merge elements
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1
        
        # Add remaining elements from left
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        
        # Add remaining elements from right    
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1
            
    return arr

# def merge_sort(arr):
 



        

print(merge_sort(arr))