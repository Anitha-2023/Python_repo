# 2. Write a function that accepts a string and prints the number of uppercase letters and lowercase letters.
#Sample input: “abcSdefPghijQkl”
#Expected Output: No. of Uppercase characters : 3 No. of Lower case Characters : 12

u_count = 0
l_count = 0
def strFunc(str):
    global u_count
    global l_count
    for i in range(len(str)):
        if str[i].isupper():
           u_count+=1
        elif str[i].islower():
           l_count+=1

str1 = input("Enter a string : ")
strFunc(str1)
print("UpperCase Characters Count : ",u_count)
print("LowerCase Characters Count : ",l_count)