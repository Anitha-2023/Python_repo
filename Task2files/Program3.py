# Write a program in Python to implement the given flowchart:
a = 10
b = 20
c = 30
avg = (a+b+c)/3
print("Average : ",avg)

if avg > a and avg >b and avg >c :
    print("Average is Higher than a,b,c")
elif avg >a and avg >b:
    print("Average is Higher than a,b")
elif avg >a and avg >c:
    print("Average is higher than a,c")
elif avg >b and avg >c:
    print("Average is higher than b,c")
elif avg >a:
    print("Average is just higher than a")
elif avg >b:
    print("Average is just higher than b")
elif avg >c:
    print("Average is just higher than c")