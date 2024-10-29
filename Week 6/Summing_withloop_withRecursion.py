def sum_with_loop(number):
    sum=0
    for i in range(1,number+1):
        sum=sum+i
    return sum

def sum_with_recursion(number):
    if number==1:
        return 1
    else:
        return number + sum_with_recursion(number-1)
def main():
    user_input=int((input("Enter the number: ")))
    result=sum_with_loop(user_input)
    result2=sum_with_recursion(user_input)
    print(result2)

if __name__=="__main__":
    main()