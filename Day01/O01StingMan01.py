
st = "hello world"
print(f"st :{st}")          # formating 'fstring' or format string -  interpolation
print(type(st))             # RTTI - runtime type identification
res = st.upper()
print(f"res :{res}")
print(f"st :{st}")

print("-" * 60)
st = "hello world"
print(f"st :{st}")

print(f"st[0] :{st[0]}")
print(f"st[6] :{st[6]}")
print(f"st[10] :{st[10]}")

# st[0] = 'H'
# print(f"st :{st}")
print("-" * 60)
print(f"st[-1] :{st[-1]}")
print(f"st[-5] :{st[-5]}")
print(f"st[-11] :{st[-11]}")

# slicing
print("-" * 60)
print(f"st[0:5] :{st[0:5]}")
print(f"st[6:11] :{st[6:11]}")
print(f"st[0:11] :{st[0:11]}")
print(f"st[0:]   :{st[0:]}")
print(f"st[:11]  :{st[:11]}")
print(f"st[:]    :{st[:]}")
print(f"st[0:11:1] :{st[0:11:1]}")
print(f"st[0:11:2] :{st[0:11:2]}")
print(f"st[0:11:2] :{st[0:11:3]}")



print("-" * 60)
print(f"st[-1:-6:-1]  :{st[-1:-6:-1]}")
print(f"st[-7:-12:-1] :{st[-7:-12:-1]}")
print(f"st[-1:-12:-1] :{st[-1:-12:-1]}")
print(f"st[-1::-1]    :{st[-1::-1]}")
print(f"st[:-12:-1]   :{st[:-12:-1]}")
print(f"st[::-1]      :{st[::-1]}")

# st1 = "hello          wor    ld"
# print(st1.count(" "))

# functions
print("-" * 60)
st = "hello world"
res = st.replace("h", "H")
print(f"res :{res}")

res = st.replace("l", "L", 1)
print(f"res :{res}")

res = st.replace("l", "L", 2)
print(f"res :{res}")

print("-" * 60)
print(dir(st))

