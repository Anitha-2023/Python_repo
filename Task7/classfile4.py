# 4.Create a Time class and initialize it with hours and minutes.
#Create a method addTime which should take two Time objects and add them.
#E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min)
#Create another method displayTime which should print the time.
#Also create a method displayMinute which should display the total minutes in the Time.
#E.g.- (1 hr 2 min) should display 62 minute.

class Timeclass:
    def __init__(self,hours1,mins1):
        self.hr1 = hours1
        self.min1 = mins1
            
    def addTime(self,h2,m2):
        temp_hr = self.hr1 + h2
        temp_min = self.min1 + m2
        x1 = temp_min//60 
        x2 = temp_min % 60
        temp_hr+=x1
        temp_min=x2
        print(f'\n\tAdded_time      : {temp_hr} hrs and {temp_min} mins') 

    def displayTime(self):
        print(f'\n\tTime            : {self.hr1} hrs and {self.min1} mins')

    def displayMinute(self):
        h = self.hr1 * 60
        h += self.min1
        print(f"\n\tTime in Minutes : {h} minutes\n")

def main():
    h1 = int(input("\nEnter the hours       : "))
    m1 = int(input("\nEnter the minutes     : "))
    h2 = int(input("\nEnter another hours   : "))
    m2 = int(input("\nEnter another minutes : "))
    timer = Timeclass(h1,m1)
    timer.addTime(h2,m2)
    timer.displayTime()
    timer.displayMinute()

if __name__ == "__main__":
    main()