s1=float(input("Enter Marks For Python:"))
s2=float(input("Enter Marks For Android:"))
s3=float(input("Enter Marks For DAV:"))
s4=float(input("Enter Marks For Computer Network:"))

total=s1+s2+s3+s4
percentage=(total/400)*100

if percentage >=90:
    grade="A+"
elif percentage >=80:
    grade="A"
elif percentage >=70:
    grade="B"
elif percentage >=60:
    grade="C"
elif percentage >=50:
    grade="D"
else:
    grade="you are Fail better luck next time"

print("\n---Student Result ---")
print("Total Marks:",total)
print("Percentage Marks:",percentage)
print("grade:",grade)
print("First Distinct")
