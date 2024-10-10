def check_age(age):
    try:
        if age<=0:
            raise ValueError("age below 0 or equal to 0")
        elif age<18:
            raise ValueError("You must be at least 18 years old.")
        elif age>=18:
            print("Age is valid. You are allowed to proceed")
    except ValueError:
        print("Try Again!")
def main():
    try:
        age=int(input("Enter age: "))
        check_age(age)
    except ValueError:
        print("Try Again!")

if __name__=="__main__":
    main()