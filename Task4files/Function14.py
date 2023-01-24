#14. Write a program in Python to find the values which are not divisible by 3 but are a multiple of 7.
#Make sure to use only higher order functions.

mlst = []
dlst = []

def multi_func():
    for i in range(1,50):
        if i % 7 == 0:
           mlst.append(i)
    return mlst
       
def div_fun(lst1):
    for j in lst1:
        if j % 3 != 0:
           dlst.append(j)
    return dlst

result = div_fun(multi_func()) #High Order Function

print("Multiple of 7 : ",mlst)
print("Values not divisible by 3 :",result)
    