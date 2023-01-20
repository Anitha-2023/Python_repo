""" 11. In the previous question, insert break after the “Good guess!” print statement. break will terminate  the while loop 
so that users do not have to continue guessing after they found the number. If the user
does not guess the number at all, print “Sorry but that was not very successful”."""


lucky_number = 25
counter = 0

while counter<5 :
    number = int(input("Enter the guessing number : "))
    counter+=1
    if number == lucky_number and counter != 6 :
       print("Good guess!!") 
       break
    elif counter !=5:
        print("Try again")
else:
    print("Sorry but that was not very successful")
    

