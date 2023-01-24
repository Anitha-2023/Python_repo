# 10.Write a program which uses filter() to make a list whose elements are even numbers between 1 and 20 (both included)

f = list(filter(lambda a : a % 2 == 0,range(1,21)))
print("Even list : ",f)



 