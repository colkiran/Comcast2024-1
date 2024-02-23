
import requests

BASE = "http://127.0.0.1:5000"

response = requests.get(BASE + "/getproduct/pepsi")
response1 = requests.get(BASE + "/getproduct/coke")
response2 = requests.get(BASE + "/getproduct/sprite")

res1 = response.json()
res2 = response1.json()
res3 = response2.json()

for ky, info in res1.items():
    print(ky)
    print("-" * len(ky))
    for k, v in info.items():
        print(k, "=>",  v)
print("-" * 60)

for ky, info in res2.items():
    print(ky)
    print("-" * len(ky))
    for k, v in info.items():
        print(k, "=>",  v)
print("-" * 60)

for ky, info in res3.items():
    print(ky)
    print("-" * len(ky))
    for k, v in info.items():
        print(k, "=>",  v)
