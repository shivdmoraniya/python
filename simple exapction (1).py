
try:
    num = int(input("Enter a number: "))

    result = 10 / num
    
    print("Result is:", result)

except ZeroDivisionError:
    print("Error: You cannot divide by zero!")

except ValueError:
    print("Error: Invalid input! Please enter a valid integer.")


