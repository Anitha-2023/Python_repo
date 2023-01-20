""" Write a program such that it asks users to “guess the lucky number”. If the correct number is guessed the program stops, otherwise it continues forever.

Modify the program so that it asks users whether they want to guess again each time. Use two variables,
 ‘number’ for the number and ‘answer’ for the answer to the question whether they want
to continue guessing. The program stops if the user guesses the correct number or answers “no”. 
(The program continues as long as a user has not answered “no” and has not guessed the correct number) """


lucky_number = 19

while True :
    number = int(input("Enter the guessing number : "))
    if number == lucky_number :
       print("Your guess right !!") 
       break
    else:
       answer = input("You guessed wrong,You want to continue guessing ? Y or N :")
       if answer.upper() == 'Y':
          continue
       else:
          break
      

