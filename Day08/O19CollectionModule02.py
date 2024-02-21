
from collections import namedtuple, deque

def results(sn, sl, mt, l1, l2):
    # science = sn
    # social = sl
    # maths = mt
    # Language1 = l1
    # Language2 = l2
    nmdTpl = namedtuple("Marks", "science social maths Language1 Language2")

    marks = nmdTpl(science=sn, social=sl, maths=mt, Language1= l1, Language2 = l2)
    return marks

res = results(89, 75, 92, 70, 69)
print(res)

print(f"Science :{res.science}")
print(f"Social  :{res.social}")
print(f"Maths   :{res.maths}")
print(f"English :{res.Language1}")
print(f"Tamil   :{res.Language2}")

# res.maths = 99

print("deque".center(60, "-"))
q1 = deque(['mike', 'peter', 'ben', 'tina'])
print(f"q1 :{q1}")

# add new elements into q1
q1.append('john')
print(f"q1 :{q1}")

q1.appendleft("kevin")
print(f"q1 :{q1}")

# remove elements from q1
res = q1.pop()
print(f"res :{res}")
print(f"q1 :{q1}")

res = q1.popleft()
print(f"res :{res}")
print(f"q1 :{q1}")

