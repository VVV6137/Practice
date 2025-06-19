def max_pairs(n, test_cases):
    results = []
    
    for a, b, x, y in test_cases:
        # Максимальное количество пар:
        max_pairs = min(a + b, x + y, min(a, x + y) + min(b, x))
        results.append(max_pairs)
    
    return results

# Чтение входных данных
n = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(n)]

# Вызов функции и вывод результатов
results = max_pairs(n, test_cases)
print(' '.join(map(str, results)))
