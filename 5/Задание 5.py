def rectangle(m, h, w):
    min_row, min_col = h, w
    max_row, max_col = -1, -1
    for i in range(h):
        for j in range(w):
            if m[i][j] == 1:
                if i < min_row:
                    min_row = i
                if j < min_col:
                    min_col = j
                if i > max_row:
                    max_row = i
                if j > max_col:
                    max_col = j
    return min_row, min_col, max_row, max_col

l = input().split()
h = int(l[0])
w = int(l[1])
m = []
for _ in range(h):
    l = input().split()
    l = list(map(int,l))
    m.append(l)
a, b, c, d = rectangle(m, h, w)
print(a - 1, b - 1, c + 1, d + 1)


