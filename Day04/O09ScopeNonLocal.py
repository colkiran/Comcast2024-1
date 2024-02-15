
def outerFun(gname):        # gname is a local variable

    def innerFun():
        nonlocal gname          # only local variable can be converted into nonlocal
        gname = "Mr." + gname
        print('Hello World')
        print(f'Hello {gname}')

    innerFun()
    print(f"outerFun :{gname}")

outerFun("Sachin")
