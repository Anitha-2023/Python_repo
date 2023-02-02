#Generate and print another tuple whose values are even numbers in the given tuple
#(1,2,3,4,5,6,7,8,9,10).

tuple1 = (1,2,3,4,5,6,7,8,9,10)
temp = []
for i in tuple1:
    if i % 2 == 0:
      temp.append(i)
print(tuple(temp))