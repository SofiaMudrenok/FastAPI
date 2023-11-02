res = set(x**2 for x in range(33) if x**2 <= 1000) or set(x**3 for x in range(11) if x**3 <= 1000)
res_sorted = sorted(res, key=lambda x: str(x)[::-1])
print(res)
print(res_sorted)

from itertools import combinations
names = ["name_" + str(x) for x in range(1, 9)]
pairs = combinations(names, 2)
for pair in pairs:
    print(pair)
