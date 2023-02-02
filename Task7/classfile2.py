# 2. Define a class named Shape and its subclass Square. The Square class has an init function which
#takes length as argument. Both classes have an area function which can print the area of the shape
#where Shape’s area is 0 by default.

class Shape:    
    def area(self):
        a1 = 0
        print("\nArea Shape : ",a1)

class Square(Shape):
    
    def __init__(self,l):
        self.len1=l
    
    def area(self):
        sq_area = 4 * self.len1
        print(f"\nArea of Square :  {sq_area} \n")

def main():
    len1 = int(input ("\nEnter the length of the Square : "))
    s1 = Shape()
    s2 = Square(len1)
    s1.area()
    s2.area()

if __name__=="__main__":
    main()