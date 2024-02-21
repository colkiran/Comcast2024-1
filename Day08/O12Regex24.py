
import re

FL = open("Story.txt", "r")
l = 0
tword = 0
eword = 0
aword = 0

for line in FL.readlines():
    l += len(line)

    res = re.findall(r'(\bt\w+)', line)
    if res:
        tword += len(res)

    res = re.findall(r'(\w+e\b)',line)
    if res:
        eword += len(res)

    res = re.findall(r'a', line)
    if res:
        aword += len(res)


print("Count of words :", l)

print("Words Starting with 't':", tword)

print("Words ending with 'e' :", eword)

print("Words that has 'a' in it :", aword)
FL.close()

#------------------------------------------------


