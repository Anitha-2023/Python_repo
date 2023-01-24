# 7. Define a function that can accept two strings as input and print the string with the maximum length
#in the console. If two strings have the same length, then the function should print both the strings line
#by line.
def maxString(s1,s2):
    s1_len = len(s1)
    s2_len = len(s2)

    if s1_len == s2_len:
        print(f'Strings with same length :\n\t{s1}\n\t{s2}')
    elif s1_len > s2_len:
        print("Longest string : ",s1)
    else:
        print("Longest String : ",s2)
    
str1 = input("Enter a String : ")
str2 = input("Enter another String : ")
maxString(str1,str2)