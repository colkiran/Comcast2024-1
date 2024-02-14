

def fact(x):
    if x == 1 or x == 0:
        return 1
    else:
        return x * fact(x-1)
a = 5
print(f"factorial of {a} is {fact(a)}")