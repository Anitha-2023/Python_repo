# 1 . Write a program that calculates and prints the value according to the given formula:
#Q= Square root of [(2*C*D)/H]
#Following are the fixed values of C and H:
#C is 50.
#H is 30.
#D is a variable whose values should be input to your program in a comma-separated sequence.

import math

class Squareroot:
    
    def __init__(self,c1,h1,val1):
        self.val =val1
        self.c = c1
        self.h =h1
            
    def calFunc(self):
        sq_list = []
        for D in self.val:
            Q = round(math.sqrt((2 * self.c * int(D))/self.h))
            sq_list.append(Q)

        print("\nsquare root value : ",sq_list)

def main():
    C = 50
    H = 30
    values = input("\nEnter a sequence : ").split(',')
    new_val = Squareroot(C,H,values)
    new_val.calFunc()

if __name__=="__main__":
    main()