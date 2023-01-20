"""
10. Write a program that asks five times to guess the lucky number. Use a while loop and a counter,
such as

While counter <= 5:
print(“Type in the”, counter, “number”
counter=counter+1
The program asks for five guesses (no matter whether the correct number was guessed or not). If the
correct number is guessed, the program outputs “Good guess!”, otherwise it outputs “Try again!”.
After the fifth guess it stops and prints “Game over!”.
"""

lucky_number = 19
counter = 0

while counter<5 :
    number = int(input("Enter the guessing number : "))
    counter+=1
    if number == lucky_number :
       print("Good guess!!") 
    else:
        if counter != 5:
            print("Try Again !")
        else:
            print("GAME OVER")


  
