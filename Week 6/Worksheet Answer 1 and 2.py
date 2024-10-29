def discount(age):
    if age<10:
        return 10
    elif age>=10 and age<=18:
        return 30
    elif age>=60:
        return 60
    else:
        return 0

def amount(traiff_standard,age): #Cannot name a variable on the function so you can't name a variable discount.
    discoun=discount(age)
    discoun=traiff_standard*discoun/100
    return traiff_standard-discoun

def main():
    x=int(input("Enter traiff_standard: "))
    y=int(input("Enter age: "))
    print(f"Final amount to be paid for {x} traiff_standard and for {y} age is {amount(x,y)}")

if __name__=="__main__":
    main()
