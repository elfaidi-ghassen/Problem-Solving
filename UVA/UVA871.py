# UVa 00871- Counting Cells in a Blob
import os, sys, collections
if os.path.exists("input.txt"):
    sys.stdin = open("input.txt")

di = [0, 0, 1, -1, 1, 1, -1, -1]
dj = [-1, 1, 0, 0, 1, -1, 1, -1]
def bfs(matrix, i, j):
    to_visit = collections.deque()
    to_visit.append((i, j))
    matrix[i][j] = "."
    size = 1
    while to_visit:
        nodei, nodej = to_visit.popleft()
        for k in range(8):
            xi = nodei + di[k]
            xj = nodej + dj[k]
            if xi < 0 or xj < 0 or xi >= n or xj >= m:
                continue
            if matrix[xi][xj] in {"0", "."}:
                continue
            matrix[xi][xj] = "."
            to_visit.append((xi, xj))
            size += 1
    return size

input_data = sys.stdin.read().split("\n")
t = int(input_data[0])
index = 2

out = []
for _ in range(t):
    matrix = []
    while index < len(input_data):
        if input_data[index] == "":
            index += 1
            break
        matrix.append(list(input_data[index]))
        index += 1
    n = len(matrix)
    if n == 0:
        print(0)
        continue
    m = len(matrix[0])
    mx = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] not in {"0", "."}:
                mx = max(mx, bfs(matrix, i, j))
    out.append(mx)
print("\n\n".join(map(str, out)))