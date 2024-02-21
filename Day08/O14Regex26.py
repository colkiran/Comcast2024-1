
import re

url = "www.google.com / search='%new hindi movies?' % / get_data2019 / fetch_data frm_1 / imdb? %hindi%movies$& / result = page1.aspx"

while(re.search("/", url)):
    res = re.search("/", url)
    print(url[:res.start()])
    url = url[res.end():]

print(url)

