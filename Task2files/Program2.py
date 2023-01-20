"""2.Write a program in Python to perform the following operation:
Ask user to choose the following option first:
If User Enter 1 - Addition
If User Enter 2 - Subtraction
If User Enter 3 - Division
If User Enter 4 - Multiplication
If User Enter 5 - Average
Ask user to enter two numbers and keep those numbers in variables num1 and num2
respectively for the first 4 options mentioned above.
Ask the user to enter two more numbers as first and second for calculating the average as
soon as the user chooses an option 5.
At the end if the answer of any operation is Negative print a statement saying “NEGATIVE”
NOTE: At a time a user can only perform one action.
"""

def arith_fun(x):

    num1 = int(input("Enter Number1 :"))
    num2 = int(input("Enter Number2 :"))
    
    if x == 1 :
       return num1 + num2
    elif x == 2:
        return num1 - num2 
    elif x == 3:
        return num1 / num2
    elif x == 4:
        return num1 * num2
    else:
        first = int(input("Enter the first number:"))
        second = int(input("Enter the second number:"))
        return (num1 + num2 + first + second)/4


if __name__ == "__main__":

    print("Select the Arithmetic Operation")
    print("\t1. Addition\n  \t2. Subtraction \n \t3. Division \n2 \t4. Multiplication\n \t5. Average")
    user_input = int(input("Enter the choice of operation : "))
    result = arith_fun(user_input)
    
    if result < 0:
        print("Result is NEGATIVE : ", result)
    else:
        print("Result : ",result)
