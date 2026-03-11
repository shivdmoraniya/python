price1 = float(input("Enter first item price: "))
price2 = float(input("Enter second item price: "))

print("Select operation:")
print("1. Addition (Total Bill)")
print("2. Subtraction (Discount)")
print("3. Multiplication (Multiple Orders)")
print("4. Division (Split Bill)")

choice = input("Enter choice (1/2/3/4): ")

if choice == '1':
    result = price1 + price2
    print("Total Bill:", result)

elif choice == '2':
    result = (price1 + price2)*5/100
    print("After Discount:", result)

elif choice == '3':
    result = price1 * price2
    print("Total for Multiple Orders:", result)

elif choice == '4':
    
    p1= int(input("Enter no of spliter:"))
    if p1 != 0 and p1 != 1:
       result = (price1 + price2) / p1
       print("Split Bill Amount:", result)
    else:
        print("Cannot divide")

else:
    print("Invalid choice")
