
def greet():
    print("Greeting Mr. Sachin, Welcome to the event.....")

def greetGst(gname):
    print(f"Greetings Mr.{gname}, Welcome to the event........")

# gname - non default argument, cty - default argument
def greetGstCty(gname, x , cty="Mumbai"):
    print(f"Greetings Mr.{gname} from {cty}, Welcome to the event........")

greet()
print("-" * 60)
greetGst("Rahul")
print("-" * 60)
greetGstCty("Sachin", 10)
greetGstCty("Sunil", 20)
greetGstCty("Rahul", 50, "Bangalore")

print("-" * 60)
def multiplyMe(x, y):
    return x * y

a = 10
b = 20
print(f"the product of {a} and {b} is :{multiplyMe(a, b)}")

# recursion - recursive calls
# factorial of a number
# fibanocci series

print("-" * 60)
# functions can return only one value

def ArithCalc(x, y):
    sum = x + y
    diff = x - y
    prod = x * y
    quot = x / y
    return sum, diff, prod, quot

print(ArithCalc(20, 8))

print("-" * 60)
# variable length arguments - *args

def multi(*numbers):           # can accept more than one value
    print(numbers)
    print(*numbers)            # unpack
    num = 1
    for number in numbers:
        num *= number
    return num

print(multi(1, 2, 3, 4, 5))

print("-" * 60)
def plyrDetails(**details):         # **kwargs - data like a dictionary
    print(details)
    for k, v in details.items():
        print(k, "=>",  v)

plyrDetails(name="Sachin", age=32, runs=55, oppn="Pak")

print("-" * 60)
# named Arguments
def admsn(fname, lname, dob, edu, desig, city, gender, mrtsts):
    print(f"Fname :{fname}")
    print(f"Lname :{lname}")
    print(f"DOB   :{dob}")
    print(f"Education :{edu}")
    print(f"Desig :{desig}")
    print(f"City :{city}")
    print(f"Gender :{gender}")
    print(f"Married :{mrtsts}")

admsn(city="Mangalore", dob="11/10/1993", gender='Male', fname="John", lname="Nixon", mrtsts="Married", edu="MBA", desig="MGR")

print("-" * 60)

def fun():
    "this is a DocString"
    # this is a comment
    print("hello world")

fun()
print(fun.__doc__)         # docstrng
print("-" * 60)

def fun1(x, y):
    """
    fun fun1(x, y)
    -------------

    1. if the function takes two integers the result will be a product of these two numbers
    2. if the function takes two strings the result will a concatenated string
    3. if the function takes two different data types then it throws an error

    """

    return x + y

print(fun1(20, 10))

help(fun1)
