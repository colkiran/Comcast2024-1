
glbX = 100

def fun(i):             # i is a local var
    global glbX        # do not assign in this line
    print(i)
    glbX = 500
    print(f"inside :{glbX}")


print(f"before :{glbX}")

fun(10)

print(f"after :{glbX}")
