d = {
   'a':645,
   'b':3987,
   'c': 93,
   'd':111,
   'e':646,
   'f': 20
}

highest_keys = []
for k in sorted(d, key=d.get, reverse=True):
    highest_keys.append(k)

print("Keys: ", highest_keys[:3])
