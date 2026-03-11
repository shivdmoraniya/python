from module import *
print("Addition")

a = int(input("Enter First Number :"))
b = int(input("Enter Second Number :"))

ans = add(a,b)
print("Addition of two numbers :",ans)

print("Substration")

x = int(input("Enter First Number :"))
y = int(input("Enter Second Number :"))

ans = sub(x,y)
print("Substration of two numbers :",ans)

print("Multiplication")

A = int(input("Enter First Number :"))
B = int(input("Enter Second Number :"))

ans = Mul(A,B)
print("Multiplication of two numbers",ans)

print("Divition")

X = int(input("Enter First Number :"))
Y = int(input("Enter Second Number :"))

try:
    ans = div(X,Y)
    print("Divition of two numbers",ans)

except ZeroDivisionError:
    print("Error: You cannot divide by zero!")
