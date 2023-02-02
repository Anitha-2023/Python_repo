"""
Write a Person class with an instance variable “age” and a constructor that takes an integer as a
parameter. The constructor must assign the integer value to the age variable after confirming the
argument passed is not negative; if a negative argument is passed then the constructor should set
age to 0 and print “Age is not valid, setting age to 0”. In addition, you must write the following instance
methods:

yearPasses() should increase age by the integer value that you are passing inside the function.
amIOld() should perform the following conditional actions:I
f age is between 0 and <13, print “You are young”.
If age is >=13 and <=19 , print “You are a teenager”.
Otherwise, print “You are old """
class Person:
    def __init__(self,age):
        if age > 0:
            self.age = age
        else:
            self.age = 0
            print("\nSetting age to 0 \n")
    
    def yearPasses(self,age1):
        age1+=self.age
        print(f"\nYear Passes : {age1}\n")

    def amIOld(self):
        print(f"Age : {self.age}\n")
        if self.age > 0 and self.age < 13:
           print("You Are Young\n")
        elif self.age >= 13 and self.age <= 19:
           print("You Are A Teenager\n")
        elif self.age > 19:
           print("You Are Old\n")
        else:
            print("Age is not Valid\n")
        
def main():
    age1 = int(input("\nEnter the age : "))
    new_person = Person(age1)
    new_person.yearPasses(10)
    new_person.amIOld()

if __name__ == "__main__":
    main()
