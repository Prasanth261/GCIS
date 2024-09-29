x=int(input("Enter start: "))
y=int(input("Enter end: "))
for i in range(y+1): #to print 1 to 10
    print(i)
for i in range(y+1): #to print 1 to 10 but only even numbers
    if i%2==0:
        print(i)
for i in range(x,y+1): #to print 1 to 10 but only odd numbers
    if i%2!=0:
        print(i)
for i in range(y,0,-1): #to print 1 to 10 but in reverse
    print(i)