class ClassDecorator:
    def __init__(self, fnc):
        self.fnc = fnc

    def __call__(self, *args):
        print("logging into the service...")
        print(self.fnc(*args))
        print("logging out of the service...")
        print("-" * 60)

    def check(self, *args):
        print("check is called")
        print(self.fnc(*args))


@ClassDecorator
def fun(x, y):
    return x + y


fun(10, 20)