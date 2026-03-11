if op=="+":
       print("Addition of given number",nm1+nm2)
   elif op=="-":
       print("Substration of given number",nm1-nm2)
   elif op=="*":
       print("Multiplication of given number",nm1*nm2)
   elif op=="/":
       print("Division of given number",nm1/nm2)
   else:
       print("Enter valid option")

try:
   num1 = int(input("Enter a first number: "))
   num2 = int(input("Enter a second number: "))
   op=(input("+,-,*,/|Enter your choice:"))


  except ZeroDivisionError:
    print("Error: You cannot divide by zero!")

except ValueError:
    print("Error: Invalid input! Please enter a valid integer.")




    


