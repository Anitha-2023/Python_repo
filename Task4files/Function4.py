#4.Write a program that accepts a hyphen-separated sequence of words as input and prints the words
#in a hyphen-separated sequence after sorting them alphabetically.

sort_list = []
str1 = input("Enter the words separated by hyphen : \n")

lst = str1.split('-')
lst.sort()

for i in lst :
    sort_list.append(i)
x = '-'.join(sort_list)

print("Sorted Sequence : ",x)