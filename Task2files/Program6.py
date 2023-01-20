# What is the output of the following code examples?

x=123
for i in x:
    print(i)

# OUTPUT : 'TypeError : 'int' object not iterable'


i = 0
while i < 5:
    print(i)
    i += 1
    if i == 3:
        break
    else:
        print("Error")

"""OUTPUT : 
    0
    Error
    1
    Error
    2
"""


count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break
"""
OUTPUT: 
    0
    1
    2
    3
    4
"""