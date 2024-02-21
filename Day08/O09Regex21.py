
import re

# \Z  -   End of the string

st = "this is a smaple text"

res = re.search(r'text\Z', st, re.I)

if res:
    print("Match found")
    print(res.group(0))
else:
    print("Match not found")


