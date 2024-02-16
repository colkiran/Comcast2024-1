
import mymodule as m

from mymodule import Player     # Player becomes local to the environment

m.greet("Ashwin")

print("-" * 60)

ply1 = Player("Rohit", 34)
ply1.get_details()
