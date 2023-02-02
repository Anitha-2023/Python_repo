#Create a class to find three elements that sum to zero from a set of n real numbers
#Input array: [-25,-10,-7,-3,2,4,8,10]
#Expected output: [[-10,2,8],[-7,-3,10]]

class Sum():
    def __init__(self,val):
        self.val = val
        
    def calSum(self):
        l = len(self.val)
        flag = 0
        print("\nResulted Array ")     
        for i in range(0,l-2):
            for j in range(i+1,l-1):
                for k in range(j+1,l):
                               
                    if(self.val[i]+self.val[j]+self.val[k] == 0):
                        flag=1
                        print(f'\n\t[{self.val[i],self.val[j],self.val[k]}]')
                        
        if flag == 0:
           print("No values found")
           
values = [-25,-10,-7,-3,2,4,8,10]
new_sum = Sum(values)
new_sum.calSum()