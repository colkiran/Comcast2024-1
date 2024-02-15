
def outerFun(greet):        # HOF - Higher Order Function
    def innerFun(sep):
        def innerMostFun(gname):
            from emojis import emojis
            emojized = emojis.encode(greet + " :" + sep + ": " + gname)
            print(emojized)
        return innerMostFun

    return innerFun

EngGrt = outerFun("Hello")
EngGrtTgr = EngGrt("tiger")

EngGrtTgr("Sheroff")






"""
EngGrt = outerFun("Hello")
TmlGrt = outerFun("Vanakam")

EngGrtSngArw = EngGrt("------>")
EngGrtDblArw = EngGrt("=======>>")
TmlGrtSngArw = TmlGrt("------->")
TmlGrtDblArw = TmlGrt("=======>>")

EngGrtSngArw("Rahul")
EngGrtDblArw("Virat")

TmlGrtSngArw("Ashwin")
TmlGrtDblArw("Karthik")

"""