# def binary_search(array_a,start,stop,target_value): 
#     mid=(start+stop)//2
#     print("printing the midpoint: ",mid)
#     if start>stop:
#         return -1
#     if array_a[mid]<target_value:
#         return binary_search(array_a,mid+1,stop,target_value)
#     if array_a[mid]>target_value:
#         return binary_search(array_a,start,mid-1,target_value)
#     elif array_a[mid]==target_value:
#         return mid


def binary_search(array,start,end,target_value):
    mid=(start+end)//2
    if start>end:
        return -1
    if array[mid]<target_value:
        return binary_search(array,mid+1,end,target_value)
    if array[mid]>target_value:
        return binary_search(array,start,mid-1,target_value)
    if array[mid]==target_value:
        return mid

def main():
    array_a=[20,30,40,60,80,90]
    target_value=int(input("Enter value to find in the array: "))
    result=binary_search(array_a,0,len(array_a)-1,target_value)
    if result==-1:
        print("Target value not found at")
    else:
        print(f"Target Value found at {result}")
main()