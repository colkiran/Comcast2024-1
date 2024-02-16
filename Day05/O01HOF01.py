
def fun(*args):
    print(args)

fun()
print("-" * 60)

fun(10)
print("-" * 60)

fun(10, 20)
print("-" * 60)

fun(10, 20, 30)

print("-" * 60)

def outerFun(fnc):
    def helper(*args):
        print("logging into the service.......")
        print(fnc(*args))
        print("logging out of the function......")
        print("-" * 60)

    return helper

def add(x, y):
    print("add function called.....")
    return x + y

def diff(x, y):
    print("diff function called......")
    return x - y

addRef = outerFun(add)
addRef(10, 20)

diffRef = outerFun(diff)
diffRef(30, 12)


