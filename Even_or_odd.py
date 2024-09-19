"""Summsary
Define a function for even then return true if the number is even and false if its not even,
then use a if function to print the apportiate message to the user"""

def even(x):
    if x%2==0:
        return True
    else:
        return False
def main():
    x=int(input("Enter a number: "))
    if even(x):
        print(f'{x} is even')
    else:
        print(f'{x} is odd')
main()