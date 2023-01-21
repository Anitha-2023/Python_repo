#3.Write a program to get the sum and multiply of all the items in a given list.


given_list = [30,5,2,10]
sum_nos = 0
multi = 1
for i in given_list:
    sum_nos += i
    multi = multi * i
print("Sum : ", sum_nos)
print("Multiply : ", multi)