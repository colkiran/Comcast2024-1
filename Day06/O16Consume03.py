
import sys

# print(sys.path)
sys.path.append("C:\Delhi")

for pth in sys.path:
    print(pth)

import gurgaon.mymodule as m
from gurgaon.mymodule import Player

m.greet("Messi")
p1 = Player("Lionel Messi", 36)
p1.get_details()
