arr=[1,3,12,42,52,8,5]
# def sort(arr):
#     for i in range(1,len(arr)):
#         j=i
#         while arr[j-1] > arr[j] and j > 0:
#             arr[j-1],arr[j]=arr[j],arr[j-1]
#             j-=1
#     print(arr)


def sort(arr):
    for i in range(1,len(arr)):
        j=i
        while arr[j-1]>arr[j] and j>0:
            arr[j-1],arr[j]=arr[j],arr[j-1]
            j-=1
def main():
    sort(arr)


main()

print(arr)


#my method

# for i in range(len(arr)):
#     j=i
#     while arr[j+1]>arr[j]:
#         arr[j+1],arr[j]=arr[j],arr[j+1]
# print(arr)

