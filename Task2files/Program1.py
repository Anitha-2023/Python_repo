"""
Write a program in Python to perform the following operation:
    If a number is divisible by 3 it should print “Consultadd” as a string
    If a number is divisible by 5 it should print “Python Training” as a string
    If a number is divisible by both 3 and 5 it should print “Consultadd - Python Training” as a string.
"""
def arith_operation(x) :
    if x % 3 == 0 and x % 5 == 0 :
       print("Consultadd - Python Training") 
    elif x % 3 == 0 :
       print("Consultadd") 
    elif x % 5 == 0 :
       print("Python Training") 
        
if __name__ == "__main__":
    a = int(input("Enter a number : "))
    arith_operation(a)
    

