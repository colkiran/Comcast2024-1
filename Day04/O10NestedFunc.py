
def outerFun(gname):

    def innerFun():

        print("hello world")
        print(f"hello {gname}")

    innerFun()

outerFun("Rahul")