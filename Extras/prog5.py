# 5. Write a program in Python to reverse a string and print only the vowel alphabet if it exists in the
#string with their index.


def fun_reverse(str1):
    str_rev = str1[::-1]
    print("\n\tReversed String : ",str_rev)
    return str_rev

def find_vowels(lstr,str_rev):    
    for i in range(lstr):
        if str_rev[i] == "a" or str_rev[i] == "e" or str_rev[i] == "o" or str_rev[i] == "i" or str_rev[i] == "u":
            print(f'\n\t\tString with index {i} : {str_rev[i]}') 

st1 = input("\nEnter the String : ")
len1 = len(st1)

rev_str=fun_reverse(st1)
find_vowels(len1,rev_str)