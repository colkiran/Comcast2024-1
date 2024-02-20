
import re
# ? - zero or one occurance of 'a'
st = "bat"

res = re.search(r'ba?t', st)

if res:
    print("Match Found......")
    print(res.group(0))     # string that matched the regex
else:
    print("Match not Found......")