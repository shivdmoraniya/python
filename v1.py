s1 = (input("Enter String: "))
v1 =('a','e','i','o','u')
count_v1 = 0
len_s1 = 0
rev_s1=""
#Count Number of Vowel in given string 
for  i in s1:
    if i in v1:
        count_v1+=1
print("vowels are: ",count_v1)

#Count Length of string (donot use len())

for i in s1:
    len_s1+=1
print("lenght of string: ",len_s1)

#Reverse string

for i in s1[::-1]:
    rev_s1 += i
print("Reverse string: ",rev_s1)
    
#Find and replace operation

s2 = "Moraniya shivam"
result = s2.replace('a','u')
print("Result: ",result)

#check whether string entered is a palindrome or not

if  s1 == rev_s1:
    print("polindrome")
else:
    print("not polindrome")
