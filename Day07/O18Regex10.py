


import re
# ()  - grouping
# | - alternation (or operator)

st = "bait"

res = re.search(r'b(oa|ai)t', st)

if res:
    print("Match Found......")
    print(res.group(0))     # string that matched the regex
else:
    print("Match not Found......")