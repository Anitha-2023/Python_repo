# 4. Find the largest and smallest number from a given list.

lst1 = [45,6856,23,72,70,34,5124]
lmax = 0
lmin = 10000000000
for i in lst1:
    if i > lmax:
        lmax = i
    if i < lmin:
        lmin = i
print("Max number : ",lmax)
print("Min number : ",lmin)

#print("max :",max(lst1))
#print("min : ",min(lst1)