# 6 .Create a list of elements such that it contains the squares of the first and last 5 elements between1 and30 (both included).

square_list = []
for i in range(1,31):
    if i<=5 or i>25 :
        square_list.append(i*i)
print(square_list)