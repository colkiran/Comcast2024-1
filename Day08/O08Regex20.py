
import re

# \A  -   Begining of the string

st = "this is a smaple text"

res = re.search(r'\Athis', st, re.I)

if res:
    print("Match found")
    print(res.group(0))
else:
    print("Match not found")


