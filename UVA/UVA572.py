import os, sys, collections
if os.path.exists("input.txt"):
    sys.stdin = open("input.txt")

di = [0, 0, 1, -1, 1, 1, -1, -1]
dj = [1, -1, 0, 0, 1, -1, 1, -1]
def bfs(matrix, init_nodei, init_nodej):
    to_visit = collections.deque([(init_nodei, init_nodej)])
    while to_visit:
        nodei, nodej = to_visit.popleft()
        for k in range(8):
            xi = nodei + di[k]
            xj = nodej + dj[k]
            if xi < 0 or xj < 0 or xi >= n or xj >= m:
                continue
            if matrix[xi][xj] in (".", "*"):
                continue
            matrix[xi][xj] = "."
            to_visit.append((xi, xj))

while True:
    n, m = map(int, input().split())
    if m == 0:
        break
    matrix = []
    for _ in range(n):
        matrix.append(list(input()))
    count = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] in ("*", "."):
                continue
            bfs(matrix, i, j)
            count += 1
    print(count)
