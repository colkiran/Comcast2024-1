
from functools import reduce, lru_cache, partial, partialmethod

# print(dir(functools))

l1 = list(range(1, 11))
print(f"l1 :{l1}")

res = reduce(lambda x, y: x + y, l1)
print(f"res :{res}")

print("LRU CACHE".center(60, "-"))
import time

def fib_without_cache(n):
    if n < 2:
        return n
    return fib_without_cache(n - 1) + fib_without_cache(n - 2)

begin = time.time()
fib_without_cache(25)
end = time.time()

print(f"time taken by the funtion without LRU Cache: {end - begin}")

print("-" * 60)

@lru_cache(maxsize=128)
def fib_with_cache(n):
    if n < 2:
        return n
    return fib_with_cache(n - 1) + fib_with_cache(n - 2)


begin = time.time()
fib_with_cache(50)
end = time.time()

print(f"The time take by FIB WITH CACHE to execute is :{end - begin}")

print("Partial".center(60, "-"))

def fun(a, b, c, d):
    return 1000 * a + 100 * b + 10 * c + 1 * d

p = partial(fun, 1, 2, 3)       # 1 for a, 2 for b and 3 for c
print(p(4))              # passing a value to d

p = partial(fun, c = 1, b = 3, d = 10)
print(p(2))

p = partial(fun, 1, 2)
print(p(3, 20))

print("partialmethod".center(60, "-"))

class Product:

    def __init__(self):
        self.__price = 45

    def __get_price(self):          # private method
        return self.__price

    def set_price(self, prc):
        self.__price = prc

    def __call__(self):
        # enable this to be called when the object is made callable
        return self.__get_price()

    set_Prdprice = partialmethod(set_price, 50)
    del_price = partialmethod(set_price, 0)

pepsi = Product()
print(pepsi())      # call the __call__
pepsi.set_Prdprice()   # call the partial method
print(pepsi())
pepsi.del_price()
print(pepsi())
pepsi.set_price(120)
print(pepsi())

