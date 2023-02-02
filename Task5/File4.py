#Create a login page backend to ask users to enter the username and password. Make sure to
#ask for a Re-Type Password and if the password is incorrect give chance to enter it again but it
#should not be more than 3 times.

user_name = input("\tUSERNAME : ")
pass_wd = input("\tPASSWORD : ")
count = 0
while count<3:
    retype = input("\t\tRe-Type Your Password again : ")
    if pass_wd == retype:
       print("\t\tSuccessfully logged in !!")
       break
    else: 
       print("\t\t\tTry Again !!")
       count+=1
else:
    print("\tPassword not Matching !")