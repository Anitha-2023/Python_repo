#1. 1. Write a program in Python to find out the character in a string which is uppercase using list comprehension.

str1 = input("Enter the string : ")
lst1 = list(str1)

upper_list = [x for x in lst1 if x.isupper()]

print(upper_list)