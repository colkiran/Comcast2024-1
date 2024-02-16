
def decorator1(func):
    def wrapper(*args):
        print("-" * 60)
        func(*args)
        print("*" * 60)

    return wrapper


def decorator2(func):
    def wrapper(*args):
        func(*args, )

    return wrapper


@decorator1
@decorator2
def fun(gname):
    print(gname)


fun("Velu")