
def outerFun(fnc):
    def helper(*args):
        print("logging in done.....")
        fnc(*args)
        print("Logging out done......")

    return helper

# decorator
@outerFun           # normalFun = outerFun(normalFun)
def normalFun(x, y):
    print(x + y)


normalFun(150, 200)

