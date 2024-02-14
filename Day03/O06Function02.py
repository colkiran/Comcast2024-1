
from collections import namedtuple
def ArithCalc(x, y):
    s = x + y
    d = x - y
    p = x * y
    q = x / y

    nmTpl = namedtuple("ArithCalc", "sum diff prod quot")
    ArthObj = nmTpl(sum = s, diff = d, prod = p, quot = q)
    return ArthObj

AObj = ArithCalc(20, 8)
print("Sum = ", AObj.sum)
print("Diff = ", AObj.diff)
print("Prod = ", AObj.prod)
print("Quot = ", AObj.quot)

