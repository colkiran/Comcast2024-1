
import requests

BASE = "http://127.0.0.1:5000/"

print("GET".center(60, "-"))
resp = requests.get(BASE + "getproduct/pepsi")
print(resp.json())

print("-" * 60)
print("PUT".center(60, "-"))

resp = requests.put(BASE + "getproduct/pepsi", data={'category': "Baverage"})
res = resp.json()

# print(res)

for ky, info in res.items():
    print(ky)
    print("-" * len(ky))
    for k, v in info.items():
        print(k, "=>", v)

print("-" * 60)
print("Delete".center(60, "-"))
resp = requests.delete(BASE + "getproduct/sprite")

res = resp.json()

for ky, info in res.items():
    print(ky)
    print("-" * len(ky))
    for k, v in info.items():
        print(k, "=>", v)
