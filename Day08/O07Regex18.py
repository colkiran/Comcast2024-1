

import re

# \b  -    word boundary

st = "thIs iS a smaple text"

res = re.search(r'\bi\w+', st, re.I)

if res:
    print("Match found")
    print(res.group(0))
else:
    print("Match not found")


