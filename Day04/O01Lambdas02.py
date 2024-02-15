
print("Filter".center(60, "-"))
l = list(range(1, 26))
print(f"list :{l}")

even_num = list(filter(lambda x: x % 2 == 0, l))
print(f"Even numbers :{even_num}")

odd_num = list(filter(lambda x: x % 2 == 1, l))
print(f"Odd Numbers :{odd_num}")

print("-" * 60)
st = "the quick brown fox jumps over the lazy dog"
print(f"st :{st}")

words = list(filter(lambda word :word, st.split()))
print(f"words :{words}")

words = list(filter(lambda word :word != "the", st.split()))
print(f"words :{words}")

print("reduce".center(60, "-"))
from functools import reduce
l = [4, 6, 9, 2, 5, 10, 7, 8]
print(f"l :{l}")

res = reduce(lambda x, y: x if x > y else y, l)
print(f"res :{res}")

l = list(range(1, 11))
res = reduce(lambda x, y: x + y, l)
print(f"res :{res}")

