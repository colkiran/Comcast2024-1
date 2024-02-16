
import mypackage.mymodule as m

from mypackage.mymodule import Player     # Player becomes local to the environment

m.greet("Rahul")

print("-" * 60)

ply1 = Player("Virat", 35)
ply1.get_details()