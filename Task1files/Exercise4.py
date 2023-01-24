# Exercise 4 :  Write a program that takes input from the user and prints it using both Python 2.x and Python 3.x Version

# Python 3.x Version

x = input("Enter a number : ")
print(x)


# Python 2.x
"""
##### INPUT Function
a = input("Enter a number:") # Takes a input value as it is without changing its datatype
a = raw_input("Enter a value :" )# Here it converts every input value to data type "String"

#### PRINT 
print "Have a good day"
print 'Great Day'
print('Good Day') ; print 'can print more text on the same line'
"""
# Exercise 8 :If one data type value is assigned to ‘a’ variable and then a different data type value is assigned to ‘a’ again. Will it change the value? If Yes then Why?

# Answer : The old value of the varible is overwritten by the new variable irrespective of the datatype

a = 34
print("Old value: ",a)
a = 35.23
print("New value: ",a)
