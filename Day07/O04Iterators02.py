
l = ['a', 'b', 'c', 'd', 'e']
print(f"l :{l}")

print("-" * 60)
iterObj = iter(l)       # l.__iter__()

while True:
    try:
        elem = next(iterObj)
        print(f"Element :{elem}")
    except StopIteration as s:
        # print("Exception Raised")
        break
