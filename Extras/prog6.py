#Write a program in Python to iterate through the string “hello my name is abcde” and print the
#string which is having an even length.

str1 = "hello my name is Anitha"
temp = str1.split(' ')
even_str = []
for i in temp:
    if len(i) % 2 == 0:
        even_str.append(i)
print("Even Length String : ", even_str)