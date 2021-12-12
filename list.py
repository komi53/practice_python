x = [1, 2, 3]
y = [4, 5, 6]
x.extend(y)
print(x)

r = [1, 2, 3, 4, 5, 6, 7, 3]
print(r.index(3, 3))

if 5 in r:
    print("exist")

r.sort()
print(r)
r.sort(reverse=True)
print(r)
r.reverse
print(r)

x = "My name is Mike."
to_split = x.split(" ")
print(to_split)

s = " aaa".join(to_split)
print(s)
