


import re

# \d    -    numbersa

st = "this 345399023 is a smaple text"

res = re.search(r'\d+', st)

if res:
    print("Match found")
    print(res.group(0))
else:
    print("Match not found")

