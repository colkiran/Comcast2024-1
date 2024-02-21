
import re

st = "the quick brown fox jumps over the lazy dog"

res = re.search(r'fox', st)

print("The string that got rejected :", st[:res.start()])

print("The string that matched the regex :", res.group(0))

print("The string that is yet to be checked :", st[res.end():])