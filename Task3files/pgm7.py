# 7 .Write a program to replace the last element in a list with another list.
#Sample input: [1,3,5,7,9,10], [2,4,6,8]
#Expected output: [1,3,5,7,9,2,4,6,8]

lst1 = [1,3,5,7,9,10]
lst2 = [2,4,6,8]
lst1.pop()
lst1.extend(lst2)
print("New List : ",lst1)