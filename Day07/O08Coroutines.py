
def get_name(surname):
    print(f"surname is {surname}")

    while(True):
        name = yield            # accepting data
        print(f"Name received is {name}")
        if surname in name:
            print(f"surname {surname} found in name")
        print("-" * 60)


coObj = get_name("Pillai")
print(coObj)
print(type(coObj))
print("-" * 60)
coObj.__next__()
coObj.send("Sachin Tendulkar")
coObj.send("Rahul Dravid")
coObj.send("Yuvraj Singh")
coObj.send("Dhanraj Pillai")