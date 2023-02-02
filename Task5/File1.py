# 1. Write a program in Python to allow the error of syntax to be handled using exception handling.
# HINT: Use SyntaxError
import sys

try :
    print(eval('6 plus 5'))
except SyntaxError:
    print("SYNTAX ERROR") 