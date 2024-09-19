def assignGrade(x):
    if x>=90:
        return "A"
    elif x<90 and x>=80: #[80,90)
        return "B"
    elif x<80 and x>=70: #[70,80)
        return "C"
    elif x<70 and x>=60: #[60,70)
        return "D"
    else:
        return "F"
def main():
    x=float(input("Enter Average marks of a student: "))
    print(f"Grade of student is {assignGrade(x)}")
main()