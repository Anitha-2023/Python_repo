# 9. Create a dictionary that contain numbers in the form(x:x*x) where x takes all the values between 1 and n(both 1 and n included).
# Sample input: n=5
# Expected output: {1:1, 2:4, 3:9, 4:16, 5:25}

n = int(input("Enter a number :"))
dict1 = {}
for key in range(1,n+1):
    dict1[key] = key*key
print(dict1)