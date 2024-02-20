
def fun():
    n = 1
    print("apples from Ooty")
    yield n
    print("Oranges from Kanpur.......")
    n += 9
    yield n
    print("Grapes from Hubli")
    n += 10
    yield n



res = fun()
print(f"res :{res}")
print(type(res))

print("-" * 60)
print(res.__next__())

print("-" * 60)
print(res.__next__())

print("-" * 60)
print(res.__next__())

# print("-" * 60)
# print(res.__next__())

print("-" * 60)

def fun1():
    for i in range(1, 11):
        yield i

fn = fun1()
print(fn.__next__())
print(next(fn))

print("-" * 60)
for x in fun1():
    print(x, end=" ")
print()

print("-" * 60)
for x in fun():
    print(x)
