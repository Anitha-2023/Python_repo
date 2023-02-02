# 6.Read doc.txt file using Python File handling concept and return only the even length string from the file. 
# Consider the content of doc.txt as given below:
#Hello I am a file
#Where you need to return the data string Which is of even length
#Make sure you return the content in The same link as it is present.

with open("doc.txt") as f:
    c = f.readlines()
    print(f"\nOriginal Content in File : {c} \n")
    print("Data string with Even length\n")
    for str in c:
        temp1 = str.split(' ')
        for x in temp1:
            if len(x) % 2 == 0:
               print(f'\t\t {x}')
    print("\n")
               