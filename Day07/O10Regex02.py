
import re

st = "bat"
# dot represents a single character
res = re.search(r'b.t', st)

if res:
    print("Match Found......")
    print(res.group(0))
else:
    print("Match not Found......")