
import re

# \w    -    alpha numeric data

st = "this is a smaple text"

res = re.search(r'\w+', st)

if res:
    print("Match found")
    print(res.group(0))
else:
    print("Match not found")
