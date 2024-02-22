
import re
# st = "the quick brown foAx jumps over the lazy dog"
#
# for i in st.split():
#     res = not(re.search(r'a|A', i))
#     if res:
#         print(i)


print("-" * 60)

def find_words_with_repeated_characters(text):
    # pattern = r'\b(\w*(\w)\w*\2\w*)\b'
    pattern = r'\b(\w+)\b(\D+)\b(\1)'
    matches = re.findall(pattern, text)
    return [match[0] for match in matches]

# Example usage:
text = "apple is a good red apple"
words_with_repeated_chars = find_words_with_repeated_characters(text)
print(words_with_repeated_chars)