d = {}
lst = [1, 3, 5, 7, 2, 4, 9]
for i in range(len(lst)):
    d["var" + str(i)] = lst[i]
print(f'(2) {d}')

for i in d:
    print(i, "=", d[i])
print("var0 + var1 =", d["var0"] + d["var1"])
print(locals())


