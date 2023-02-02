# 2 . Write a program to construct a dictionary from the two lists containing the names of students andtheir corresponding subjects.
#  The dictionary should map the students with their respective subjects.Let’s see how to do this using for loops and dictionary comprehension.
#HINT - Use Zip function also
#Sample input: students = ['Smit', 'Jaya', 'Rayyan'] subjects = ['CSE', 'Networking', 'Operating System']
#Expected output: {‘Smit’ : ’CSE’ , ’Jaya’ : ’Networking’ , ’Rayyan’ : ’Operating System’}

students = ['Smit', 'Jaya', 'Rayyan']
subjects = ['CSE', 'Networking', 'Operating System']

dict1 = {}

#  USING FOR LOOPS
for keys in students:
    for values in subjects:
        dict1[keys]=values
        subjects.remove(values)
        break       
print("Dictionary using For Loops : ",dict1)


#  USING DICTIONARY COMPREHENSION
"""
students = ['Smit', 'Jaya', 'Rayyan']
subjects = ['CSE', 'Networking', 'Operating System']

dict2 = {keys:values for keys,values in zip(students,subjects)}
print("DICTIONARY COMPREHENSION : ",dict2)
"""

# Using Zip Functions
"""
students = ['Smit', 'Jaya', 'Rayyan']
subjects = ['CSE', 'Networking', 'Operating System']

dict3=dict(zip(students,subjects))
print("Zip Function : ",dict3)
"""