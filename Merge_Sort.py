arr=[1,123,53,13,643,13,5,3]

def merge_sort(arr):
    if len(arr) > 1:

        ratio = 0.5  #50-50 split
        split_index = int(len(arr) * ratio)
        left_arr = arr[:split_index]
        right_arr = arr[split_index:]
        
        merge_sort(left_arr)
        merge_sort(right_arr)
        

        i=0
        j=0

        
        for k in range(len(arr)):
            if i < len(left_arr) and j < len(right_arr):
                if left_arr[i] < right_arr[j]:
                    arr[k] = left_arr[i]
                    i += 1
                else:
                    arr[k] = right_arr[j]
                    j += 1

            
            elif i < len(left_arr):
                arr[k] = left_arr[i]
                i += 1

            else:
                arr[k] = right_arr[j]
                j += 1
            
    return arr

# def merge_sort(arr):
 



        

print(merge_sort(arr))