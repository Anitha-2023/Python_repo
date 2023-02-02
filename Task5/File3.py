#Write a program to handle an error if the user entered a number more than four digits it should
#return “The length is too short/long !!! Please provide only four digits”

class NumberLongerException(Exception):
    pass
try:
    a = int(input("Enter a number : "))
    if a > 9999 :
        raise NumberLongerException
except NumberLongerException:
    print("Number Too Long,Please provide only four digits !!")