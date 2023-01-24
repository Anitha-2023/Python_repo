"""9.Write a function called showNumbers that takes a parameter called limit. It should print all the
numbers between 0 and limit with a label to identify the even and odd numbers.
Sample input: show Numbers(3) (where limit=3)
Expected output:
0 EVEN1 ODD
2 EVEN
3 ODD """

def showNumbers(lmt):
    for i in range(0,lmt+1):
        if i % 2 == 0:
           print(f'{i} Even')
        else:
            print(f'{i} ODD') 

limit = int(input("Enter the limit : "))
showNumbers(limit)