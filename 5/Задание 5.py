def rectangle(matrix, h, w):
    min_row, min_col = h, w
    max_row, max_col = -1, -1
    for i in range(h):
        for j in range(w):
            if matrix[i][j] == 1:
                if i < min_row:
                    min_row = i
                if j < min_col:
                    min_col = j
                if i > max_row:
                    max_row = i
                if j > max_col:
                    max_col = j
    return min_row, min_col, max_row, max_col

h, w = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(h)]
top_left_row, top_left_col, bottom_right_row, bottom_right_col = rectangle(matrix, h, w)
print(top_left_row - 1, top_left_col - 1, bottom_right_row + 1, bottom_right_col + 1)

