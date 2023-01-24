# 15.Write a program in Python to multiply the elements of a list by itself using a traditional function
#and pass the function to map() to complete the operation.

def fun (x):
    return x * x
    
list1 = [2,5,13,14,10]
m = list(map(fun,list1))
print("Multiplied list :",m)