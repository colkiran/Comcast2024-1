
import collections

st = "abcaabbccdddabcdadzzxxcca"

res = collections.Counter(st)

print(res)


"""
a = ?
b = ?
c = ?
d = ?
"""
# frequency = {}
# for i in st:
#     if i in frequency:
#         frequency[i] += 1
#     else:
#         frequency[i] = 1
# print(frequency)


#
# def find_repeated(ip_string):
#
#     repeated_char = set()
#
#     for alpha in ip_string:
#
#         if ip_string.count(alpha) > 1:
#
#             repeated_char.add(alpha)
#
#     return repeated_char
#
#
# ip_string = "abbbababbaa"
#
# result = find_repeated(ip_string)
#
# print(result)