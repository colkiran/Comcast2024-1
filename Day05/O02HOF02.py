
def callme():
    print("Apples from Ooty.....")
def fun(fnc):
    print("Hello.......")
    fnc()
    print("Hi.....")
    print("-" * 60)

    def defineMe():
        print("Oranges from Kanpur......")

    return defineMe

def funcallBack(fnc):
    print("Mera Bharath Mahan......")
    fnc()
    print("India is great.....")


funcallBack(fun(callme))
