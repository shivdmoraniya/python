
class NegativeNumberError(Exception):
    def __init__(self, value):
        self.value = value
        super().__init__(f"Negative numbers are not allowed: {value}")

def check_number(num):
    if num < 0:
        raise NegativeNumberError(num)  
    else:
        print(f"Good! You entered a positive number: {num}")

try:
    number = int(input("Enter a number: "))
    check_number(number)

except NegativeNumberError as e:
    print("Caught an exception:", e)

except ValueError:
    print("Error: Invalid input! Please enter a valid integer.")
