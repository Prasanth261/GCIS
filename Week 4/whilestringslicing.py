def pos_loop(string):
    count=0

    while count<len(string):
        print(string[count])
        count+=1
    print(string)

def neg_loop(string):
    count=1

    while count<=len(string):
        print(string[-(count)])
        count+=1

def main():
    string=str(input("Enter a string: "))
    pos_loop(string)
    neg_loop(string)

main()