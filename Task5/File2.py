#2.Write a program in Python to allow the user to open a file by using the argv module. If the
#entered name is incorrect throw an exception and ask them to enter the name again. Make sure to use read only mode.

import sys

try:
    with open(sys.argv[1], 'r') as f:
        contents = f.read()        

except FileNotFoundError:
    print("\n\tIncorrect file name,enter filename again\n")


# Command Line - python3 File2.py doc1.txt 