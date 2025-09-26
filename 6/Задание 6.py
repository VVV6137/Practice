def pairs(n, t):
    results = []
    for a, b, x, y in t:
        pairs = min(a + b, x + y, min(a, x + y) + min(b, x))
        results.append(pairs)
    return results

n = int(input())
t = []
for _ in range(n):
    l = input().split()
    l = tuple(map(int,l))
    t.append(l)
results = pairs(n, t)
r = ""
for i in results:
    r += str(i)
    r += " "
print(r)
