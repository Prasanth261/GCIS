import random 
def gen_3():
    list1=[]
    for i in range(3):
        list1.append(random.randint(1,100))
    tuple1=tuple(list1)
    print(tuple1)
    print(type(tuple1))
gen_3()