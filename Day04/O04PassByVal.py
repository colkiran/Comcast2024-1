
def fun(x):
    print(x)
    x += 50
    print(f"x inside the function :{x}")

y = 100
print(f"y before the function call :{y}")
fun(y)
print(f"y after the function call :{y}")
