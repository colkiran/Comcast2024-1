
# conversions
print("{val} {val} {val}".format(val = "A"))
print("{val!s} {val!r} {val!a}".format(val = "A"))

print("-" * 60)
print("The number {num} {num} {num}".format(num = 36))
print("The number {num} {num:f} {num:b}".format(num = 36))
print("The number {num:10} {num:f} {num:b}".format(num = 36))
print("The number {num:5} {num:f} {num:b}".format(num = 36))
print("The number {num:5} {num:f} {num:b}".format(num = 363534534))

print("-" * 60)
#alignmen
print("{num:15}Tendulkar".format(num=36))
print("{num:15}Tendulkar".format(num="Sachin"))
print("{}".format("Sachin Tendulkar"))
print("{:.6}".format("Sachin Tendulkar"))

from math import pi, e
print("{pi:10.2}".format(pi=pi))
print("{pi:10.3}".format(pi=pi))
print("{pi:10.4}".format(pi=pi))
print("{pi:10.5}".format(pi=pi))

print("-" * 60)
print("{num:>15}Tendulkar".format(num="Sachin"))
print("{num:^15}Tendulkar".format(num="Sachin"))
print("{num:<15}Tendulkar".format(num="Sachin"))

print("{num:-^60}".format(num="Sachin"))
print("Sachin".center(60, "-"))

print("-" * 60)
print("{num:010}".format(num=10))
print("{num:010}".format(num=2458))
print("{num:010}".format(num=12345))

print("one googol is {}".format(10 ** 100))
print("one googol is {:,}".format(10 ** 100))       # thousands seperator

print("{0:10.2f}\t{1:10.2f}".format(pi, -pi))