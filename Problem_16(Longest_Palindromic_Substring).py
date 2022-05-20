# Write a program to find the longest Palindrome in a string.[ Longest palindromic Substring]

str1 = input("Enter the string : ")
res = []

for i in range(len(str1)):
    for j in range(len(str1), i + 1, -1):
        if str1[i:j] == str1[i:j][::-1]:
            res.append(str1[i:j])

if len(res) == 0:
    print("No palindromic sub-string found !")
else:
    print(max(res, key=len))
