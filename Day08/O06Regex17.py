
import re

# \S   -    non space characters

st = "this@#$232342   is a smaple text"

res = re.search(r'\S+', st)

if res:
    print("Match found")
    print(res.group(0))
else:
    print("Match not found")


