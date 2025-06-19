def pairs(n, test_cases):
    results = []
    for a, b, x, y in test_cases:
        pairs = min(a + b, x + y, min(a, x + y) + min(b, x))
        results.append(pairs)
    return results

n = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(n)]
results = pairs(n, test_cases)
print(' '.join(map(str, results)))
