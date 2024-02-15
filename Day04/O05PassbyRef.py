
def fun(lst):
    print(f"list :{lst}")
    lst.extend([6, 7, 8, 9, 10])
    print(f"lst after modification :{lst}")


lst = list(range(1, 6))
print(f"lst before the function call :{lst}")
fun(lst)
print(f"lst after the function call :{lst}")

