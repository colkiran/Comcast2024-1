
import re

# ^ and $

st = "the quick brown fox jumps over the lazy dog"
print(f"st :{st}")

# res = re.match('^the', st)
# match function will match only at the begining of the string
res = re.search('dog$', st)

if res:
    print("Match Found......")
    print(res.group(0))     # string that matched the regex
else:
    print("Match not Found......")