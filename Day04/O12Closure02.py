
def outerFun(greet):
    #simple curry
    def innerFun(name):

        print(greet, name)

    return innerFun

#---------------------
EngGrt = outerFun("Hello")
TmlGrt = outerFun("Vanakam")
KanGrt = outerFun("Namaskara")

EngGrt("Sachin")
TmlGrt("Ashwin")
KanGrt("Rahul")
