import time

def outerFun(fnc):
    def helper(*args):
        start_time = time.time()
        print("Time started")
        fnc(*args)
        print("Time Ended")
        end_time = time.time()

        print(f"Total time taken to execute the func is {end_time - start_time}")

    return helper


@outerFun  # normalfun=outerFun(normalfun)
def normalfun(x):
    time.sleep(x)


normalfun(2)
