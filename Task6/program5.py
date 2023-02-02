#Write an example on decorators.


def deco_fun(func):
    def inner():
        print("First Line in inner function")
        func()
        print("End of inner function")
    return inner

@deco_fun
def new_fun():
    print("Hi Decorator Function")
new_fun()