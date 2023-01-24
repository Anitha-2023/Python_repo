# 13. Flatten the list [1,2,3,4,5,6,7] into 1234567 using reduce().

from functools import reduce

lst = [1,2,3,4,5,6,7]
def fun(a,b):
    return 10*a+b

flatten_list = reduce(fun,lst)
print(flatten_list)