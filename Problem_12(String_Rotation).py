# Write a Code to check whether one string is a rotation of another.

str1 = input("Enter 1st string : ")
str2 = input("Enter 2nd string : ")

temp = str1 + str1

if str2 in temp:
    print("YASS")
else:
    print("NO YASS ;)")
