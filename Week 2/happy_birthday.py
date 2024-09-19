while True:
    try:

        Data_N=input("Enter Name: ")
        Data_D=int(input("Enter Birth day of the month: "))
        Data_M=int(input("Enter Birth Month: "))
        Data_Y=int(input("Enter birth Year: "))
        print(f"{Data_N},your birthday is on {Data_D}/{Data_M}/{Data_Y}")
    except:
        print("Try Again! Remember its numbers.")