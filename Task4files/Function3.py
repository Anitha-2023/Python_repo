# 3 .Create a() function that takes a list and returns a new list with unique elements of the first list.

new_list = []
def funList(lst):
    for num in lst:        
        if num not in new_list:
           new_list.append(num)
    return new_list       

num_list = []
num_list = input("Enter the list of numbers : ").split(',')
a = funList(num_list)
print("Unique List of Numbers : ",a)


"""
num_list = []
num_list = input("Enter the list of numbers : ").split(',')
a = set(num_list)
b = list(a)

print("Unique List of Numbers : ",b)
"""