total_sum=0

while True:
    try:
        numerator=input("Enter a numerator: ")
        if numerator == "*":
            break
        numerator = float(numerator)
        denominator=input("Enter a numerator: ")
        if denominator == "*":
            break
        denominator = float(denominator)

        if denominator == 0:
            print("Can't divide by 0")
            continue

        result=numerator/denominator
        print(f"Result of division = {result}")
        total_sum+=result

    except ValueError:
        print("Non-numeric value entered, Please enter a value number.")

print(f"Final total sum of all results: {total_sum}")