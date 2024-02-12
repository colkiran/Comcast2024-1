
st = "kiran1234"
# res = "narik4321"

def rev(st):
    res1 = []
    res2 = []
    for i in range(0, len(st)):
        if st[i].isnumeric():
            res1.append(st[i])
        else:
            res2.append(st[i])
    return res2[::-1] + res1[::-1]

res = rev(st)
print("".join(res))
