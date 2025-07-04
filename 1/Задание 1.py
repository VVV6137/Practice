import random

def time(n, pyramid):
    dp = [[0] * (i + 1) for i in range(n)]
    dp[0][0] = pyramid[0][0]
    for i in range(1, n):
        for j in range(i + 1):
            if j == 0:
                dp[i][j] = dp[i - 1][j] + pyramid[i][j]
            elif j == i:
                dp[i][j] = dp[i - 1][j - 1] + pyramid[i][j]
            else:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + pyramid[i][j]
    min_time = min(dp[n - 1])
    return min_time, dp

def path(n, pyramid, dp):
    min_index = dp[n - 1].index(min(dp[n - 1]))
    path = []
    current_index = min_index
    for i in range(n - 1, -1, -1):
        path.append(pyramid[i][current_index])
        if i > 0:
            if current_index > 0 and dp[i - 1][current_index - 1] < dp[i - 1][current_index]:
                current_index -= 1

    path.reverse()
    return path

n = int(input())
pyramid = []
for i in range(n):
    level = [random.randint(1, 100) for _ in range(i + 1)]
    pyramid.append(level)

for level in pyramid:
    print(" ".join(map(str, level)))
time, dp = time(n, pyramid)
path = path(n, pyramid, dp)
print("Минимальное время пути:", time)
print("Сам путь", " ".join(map(str, path)))
