

import re
# {n,m} - min n occurances and max m occurances of 'a'
st = "baaaaaaaaat"

res = re.search(r'ba{3,8}t', st)

if res:
    print("Match Found......")
    print(res.group(0))     # string that matched the regex
else:
    print("Match not Found......")