# Write a program which accepts a sequence of comma-separated numbers from console and generates a list and a tuple which contains 
# every number in the form of string.
#Sample input: 34,67,55,33,12,98
#Expected output: [‘34’,’67’,’55’,’33’,’12’,’98’] (‘34’,’67’,’55’,’33’,’12’,’98’) 

num = input("Enter the sequence of numbers :")
new_list = num.split(',')
new_tuple = tuple(new_list)        
print("new list :",new_list)
print("new tuple",new_tuple)