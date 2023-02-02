#Write a program in python to print the pair of numbers whose sum is equal to the resultnumber that is let's say 8.
#x=[1,2,3,4,5,6,7,8,9,-1]

x=[1,2,3,4,5,6,7,8,9,-1]
dict1 = {}
for i in x:
    x.remove(i)
    for j in x:
        if i+j == 8:
            dict1[i]=j
print("Pair of values make 8 : ",dict1) 

