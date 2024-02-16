
class ClassDecorator:
    def __init__(self, fnc):
        self.fnc = fnc
    def __call__(self, *args):              # innerFun
        print("Logging into the service......")
        print(self.fnc(*args))
        print("Logging out of the service......")
        print("-" * 60)

@ClassDecorator
def fun(x, y):
    print(f"Addition of {x} and {y}")
    return x + y

@ClassDecorator
def Diff(x, y):
    print(f"Difference of {x} and {y}")
    return x - y

@ClassDecorator
def prod(x, y):
    print(f"Product of {x} and {y}")
    return x * y



fun(20, 30)
Diff(90, 76)
prod(20, 145)
