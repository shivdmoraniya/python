nm1=int(input("Enter First Number:"))
nm2=int(input("Enter Second Number:"))
op=(input("+,-,*,/|Enter your choice:"))


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
     
