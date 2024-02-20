
import re
# * - zero or more occurance of 'a'
st = "baaaaaaaaaaaaaaaaaaaaaaaaaaaaat"

res = re.search(r'ba*t', st)

if res:
    print("Match Found......")
    print(res.group(0))     # string that matched the regex
else:
    print("Match not Found......")