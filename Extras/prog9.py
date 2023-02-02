# Write a program to find out the occurrence of a specific character from an alphanumeric string.
#Sample input: 12abcbacbaba344ab
#Expected output: a=5 b=5 c=2
#NOTE: Make sure to avoid counting the occurrence of numeric values in the string.

string1 = "12abcbacbaba344ab"
str_list = []
for i in string1:
    if i.isnumeric()==False:
        str_list.append(i)

print("\na = ",str_list.count('a'))
print("\nb = ",str_list.count('b'))
print("\nc = ",str_list.count('c'))