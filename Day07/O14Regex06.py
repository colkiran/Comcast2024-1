
import re
# {n} - exactly n occurances of 'a'
st = "baaat"

res = re.search(r'ba{3}t', st)

if res:
    print("Match Found......")
    print(res.group(0))     # string that matched the regex
else:
    print("Match not Found......")