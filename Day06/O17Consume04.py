

import sys

# print(sys.path)
# sys.path.append("C:\Delhi")

for pth in sys.path:
    print(pth)

import gurgaon.mymodule as m
from gurgaon.mymodule import Player

m.greet("Ronaldo")
p1 = Player("Cristiano Ronaldo", 37)
p1.get_details()
