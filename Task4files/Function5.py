"""5. Write a program that accepts a sequence of lines as input and prints the lines after making all
characters in the sentence capitalized. """
#Sample input: Hello world Practice makes man perfect
#Expected output: HELLO WORLD PRACTICE MAKES MAN PERFECT

lines = []
print("Enter the Sequence of Lines")
while True:
    sent = input()
    if sent != '':
        lines.append(sent.upper())
    else:
        break

for sentence in lines:
    print(sentence)


#sent = input("Enter Sequence of Lines :")
#print(sent.upper())
