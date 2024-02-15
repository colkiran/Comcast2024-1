
d1 = [(x, y) for x in range(3) for y in range(3)]
print(d1)

print("-" * 60)
d2 = [(x, y) for x in range(1, 6) for y in range(1, x+1)]
print(d2)

print("-" * 60)
print([x ** 2 if x % 2 == 0 else x ** 3 for x in range(1, 11)])

players = {
    'sachin': [350, 250, 300, 400, 385],
    'rahul': [200, 300, 450, 150, 185],
    'sehwag':[300, 350, 425, 400, 360],
    'sourav':[180, 250, 200, 350, 150],
    'laxman':[345, 300, 200, 150, 190],
    'yuvraj':[190, 150, 120, 250, 275]
}

print(f"Players :{players}")
print("-" * 60)

print(f"Sachin :{players['sachin']}")
print(f"Sachin :{sum(players['sachin'])}")

print("-" * 60)
scores = {k: v for k, v in players.items()}
print(f"scores :{scores}")

print("-" * 60)
scores = {k: sum(v) for k, v in players.items()}
print(f"scores :{scores}")

print("-" * 60)
scores = [runs for runs in players.values()]
print(f"scores :{scores}")

print("-" * 60)
plyrs = [player for player in players.keys()]
print(f"plyrs :{plyrs}")

print("-" * 60)
avg_scr = {name: (lambda scr: sum(scr) / len(scr))(score)
            for name, score in players.items()}
print(f"Average Score :{avg_scr}")

print("-" * 60)
def avg(lst):
    return sum(lst) / len(lst)

avg_scr = {name: avg(score) for name, score in players.items()}
print(avg_scr)

print("-" * 60)
basic = [{x :(lambda par: "Mr." + par) ('Sachin {}'.format(x))
          for x in range(1, 6)}]
print(basic)

print("-" * 60)
scores = [scr for scr in players.values()]
print(f"scores :{scores}")

print("-" * 60)
scores = [scr for score in players.values() for scr in score]
print(f"scores :{scores}")

print("-" * 60)
scores = [scr for score in players.values() for scr in score if scr >= 200]
print(f"scores :{scores}")

# print("=" * 60)
# lst  = [[350, 250, 300, 400, 385], [200, 300, 450, 150, 185], [300, 350, 425, 400, 360], [180, 250, 200, 350, 150], [345, 300, 200, 150, 190], [190, 150, 120, 250, 275]]
#
# for i in lst:
#     for j in i:
#         if j >= 200:
#             print(j, end=" ")
# print()

print("-" * 60)
scores = {name: [scr for scr in score if scr > 200]
                for name, score in players.items()}
print(f"scores :{scores}")

print("-" * 60)
st = "the quick brown fox jumps over the lazy dog"
print(f"st :{st}")

print("-" * 60)
res = [word for word in st.split()]
print(f"res :{res}")

print("-" * 60)
res = {word: len(word) for word in st.split()}
print(f"res :{res}")