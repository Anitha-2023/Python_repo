# Create a new list which contains the specified numbers after removing the even numbers from a predefined list.

lst1 = [47,31,80,61,20,28,12,5,3,91]
new_list = []
for i in lst1:
    if i % 2 != 0:
        new_list.append(i)
print("New List : ",new_list)