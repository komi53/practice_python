d = {"x": 10, "y": 20}
print(d)

print(d.keys())

d2 = {"x": 1000, "j": 500}
print(d.update(d2))

print(d.get("x"))


d.pop("x")

print(d)
