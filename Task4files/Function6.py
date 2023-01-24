#6. Define a function that can receive two integral numbers in string form and compute their sum and
#print it in the console.

def sumFunc(n1,n2):
    a=int(n1)
    b=int(n2)
    return a+b

num1 = input("Enter number1 : ")
num2 = input("Enter number2 : ")
s = sumFunc(num1,num2)
print("Sum of two numbers : ", s)