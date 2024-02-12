
st = "hello world"
print(f"st :{st}")
# mike -> dave

print("Maketrans".center(60, "-"))
a = 'helowrd'
b = 'HELOWRD'
# length of a and b should be the same
resTbl = st.maketrans(a, b)
print(resTbl)

print("Translate".center(60, "-"))
res = st.translate(resTbl)
print(res)

print("format".center(60, "-"))
# C style of formatting - printf
format = "Welcome %s, what a %s player"
print(format)
values = ("Sachin", "class")        # tuple
print(values)
print("-" * 60)
print(format, values)
print("-" * 60)
print(format % values)
print("-" * 60)
print("Welcome %s, what a %s player" % ("Rahul", "Class"))
print("Welcome %s, what a %s player with a rating of %.3f" % ("Sachin",
                                                "class", 4.8))

# unix style
from string import Template
tmpl = Template("Welcome $name, what a $adj player")
print(tmpl)
res = tmpl.substitute(name = "Sachin", adj = "superb")
print(res)

print("-" * 60)
# format of python string
print("Welcome {}, what a {} player".format("Sachin", "class"))
print("Welcome {}, what a {} player for {}".format("Sachin", "class", "India"))
print("Welcome {}, what a {} player for {}".format("class","India", "Sachin"))

print("Welcome {0}, what a {2} player for {1}".format("Sachin", "class", "India"))

print("-" * 60)
print("Welcome {0} with a rating {rating}, what a {2} player for {1}".format( "class", "India", "Sachin", rating=4))

print("-" * 60)
print("Welcome {0} with a rating {rating:.3f}, what a {2} player for {1}".format( "class", "India", "Sachin", rating=4.8764))

# interpolation
from math import pi, e
print(f"PI = {pi} and eulers constant e = {e}")

print("-" * 60)
print("PI = {} and Eulers constant e = {}".format(pi, e))

print("-" * 60)
full_name = ['Sachin', "Tendulkar"]
print(full_name)
print("Mr.{name}".format(name = full_name))
print("Mr.{name[0]} {name[1]}".format(name = full_name))

print("-" * 60)
print(__name__)         # double underscore name - dunder name
import math
print(math.__name__)

print("the {mod.__name__} module gives the value of pi = {mod.pi} and eulers constant e = {mod.e}".format(mod = math))
