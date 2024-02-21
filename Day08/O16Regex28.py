

import re
st = """
the quick brown fox jumps over the lazy dog.
the quick brown fox jumps over the lazy dog.
the quick brown fox jumps over the lazy dog.
the quick brown fox jumps over the lazy dog.
the quick brown fox jumps over the lazy dog.
the quick brown fox jumps over the lazy dog.
the quick brown fox jumps over the lazy dog.
the quick brown fox jumps over the lazy dog.
the quick brown fox jumps over the lazy dog.
the quick brown fox jumps over the lazy dog.
"""
for match in re.finditer(r'\bt\w+', st):
    s = match.start()
    e = match.end()
    # print(match)
    print(f"Match found between {s} and {e} :{st[s:e]}")
