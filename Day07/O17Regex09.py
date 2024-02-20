
import re
 # [] - character class - one character

st = "bxt"

# res = re.search(r'b[a-zA-Z0-9]t', st)
# res = re.search(r'b[aeiou]t', st)
res = re.search(r'b[^aeiou]t', st)

if res:
    print("Match Found......")
    print(res.group(0))     # string that matched the regex
else:
    print("Match not Found......")