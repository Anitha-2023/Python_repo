# 8. Define a function which can generate and print a tuple where the values are square of numbers
#between 1 and 20 (both 1 and 20 included).

def funcTuple():
    lst = []
    for i in range(1,21):
        lst.append(i * i)
    print(tuple(lst))

funcTuple()