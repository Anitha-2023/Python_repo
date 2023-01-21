# 8. Create a new dictionary by concatenating the following two dictionaries:
#Sample input: a={1:10,2:20} b={3:30,4:40}
#Expected output: {1:10,2:20,3:30,4:40}

dict1_a = {1:10 , 2:20}
dict2_b = {3:30,4:40}
new_dict = dict1_a.copy()
new_dict.update(dict2_b)
print("New Dict : ",new_dict)
print(dict1_a)

# Another method
"""
dict1_a = {1:10 , 2:20}
dict2_b = {3:30,4:40}
dict3 = dict1_a.copy()
for key, values in dict2_b.items() :
    dict3[key] = values
print(dict3)

"""
