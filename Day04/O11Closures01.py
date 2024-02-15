

def outerFun(gname):

    def innerFun():

        print("hello world")
        print(f"hello {gname}")

    return innerFun

outerFun("Sachin")()            # calls the inner function

print("-" * 60)
inRef = outerFun("Rahul")

for i in range(1, 11):
    for j in range(1, i+1):
        pass

inRef()                     # calls the innerFun
