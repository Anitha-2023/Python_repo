#Create two lists such as even_list and odd_list
#Ask user to enter a number in the range of 1,50 and make sure if the entered number is even, 
# append it to the even_list and if the entered number is odd append it to the odd_list.
#Keep that in mind you can only add 5 items in each list
#Make sure once you enter all the 5 elements, calculate the sum of the list and return the maximum of the list.

from functools import reduce

def sum(a,b):
    return int(a)+int(b)

even_list = []
odd_list = []
values = input("\nEnter the numbers in range of 1-50 : ").split(',')
even_count = 0
odd_count = 0
for i in values:
    if int(i) % 2 == 0 and even_count < 5:
        even_list.append(i)
        even_count+=1
    elif int(i) % 2 != 0 and odd_count < 5:
        odd_list.append(i)
        odd_count+=1

print("\nEven Number List : ",even_list)
print("\nOdd Number List : ",odd_list)
#print(type(even_list))
print("\nSum of Even list : ", reduce(sum,even_list))
print("\nSum of Odd list : ", reduce(sum,odd_list))