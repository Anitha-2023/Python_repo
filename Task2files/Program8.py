""" Write a program that accepts a string as an input from the user and calculate the number of digits and letters.
Sample input: consul72
Expected output: Letters 6 Digits 2 """

a = input("Enter the string :")
lcount = 0
dcount = 0
for i in range(len(a)):
    if a[i].isnumeric():
       dcount += 1
    else:
       lcount +=1
print("Letters : ",lcount)  
print("Digits : ",dcount)

