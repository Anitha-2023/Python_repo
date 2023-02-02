#4.4. Write a program in Python using generators to reverse the string.
#Input String = “Consultadd Training”

str1 = "Consultadd Training"

def generator_fun(s1):
    yield s1[::-1]

rev_str = generator_fun(str1)

print("Given String : ",str1)
print("Reversed String : ",next(rev_str))