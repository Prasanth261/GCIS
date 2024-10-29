

def series(number):
    if number==0:
        return series(number)
    else:
        return number+series(number-1)


print(series(4))



# number=10
# list1=[0]
# for i in range(number):
#     if sum(list1)==0:
#         list1.append(1)
#     else:
#      list1.append(list1[len(list1)-1]+list1[len(list1)-2])

# print(list1)

