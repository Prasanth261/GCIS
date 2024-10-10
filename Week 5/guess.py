def guessing():
    try: 
        num=input("Pick a number from 1-10: ")
        no=int(num)
        if no<1 or no>10:
            raise ValueError("pick bet 1-10")
        else:
            print("You picked,no")
    except ValueError:
        print("Enter a integer!")
guessing()