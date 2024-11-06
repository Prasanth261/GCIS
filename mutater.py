def mutator(list1,int1):
    a_list=list1
    an_int=int1
    print(a_list)
    print(an_int)
    an_int=an_int*5
    a_list[0]=a_list[0]*5
    print(a_list)
    print(an_int)
def main():
    mutator([2,65],123)
if __name__=="__main__":
    main()