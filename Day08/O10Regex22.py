
import re

# back tracking - reusing regular expression

st = "good blood bad blood"

# \2 is recalling the second grouping
res = re.search(r'(\w+)\s(\w+)\s(\w+)\s(\2)', st)

if res:
    print("Match found....")
    print(res.group(0))
else:
    print("Match not found....")