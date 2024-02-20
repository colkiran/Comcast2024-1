

import re
# {n,} - min n occurances and max infinite occurances of 'a'
st = "baat"

res = re.search(r'ba{3,}t', st)

if res:
    print("Match Found......")
    print(res.group(0))     # string that matched the regex
else:
    print("Match not Found......")