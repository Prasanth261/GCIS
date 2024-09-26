count=0
while True:
    x=input("Enter x to exit: ")
    print(count)
    count+=1
    if x=="x":
        print("exited")
        break
    elif x=="y":
        continue