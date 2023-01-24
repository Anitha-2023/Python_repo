#12.Write a function to compute 5/0 and use try/except to catch the exceptions

def fun():
    try:
        value = 5/0
    except Exception as e:
        print(e)

    #except:
       # print("Divide by zero error")

fun()