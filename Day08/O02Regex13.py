

import re

# \W    -    Special characters

st = "this !@#$   %^&* is a smaple text"

res = re.search(r'\W+', st)

if res:
    print("Match found")
    print(res.group(0))
else:
    print("Match not found")

