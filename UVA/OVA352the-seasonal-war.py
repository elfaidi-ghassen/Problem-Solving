from collections import deque

di = [0, 0, 1, -1, 1, -1, 1, -1]
dj = [1, -1, 0, 0, 1, 1, -1, -1]
def bfs(matrix, init_i, init_j):
    to_visit = deque()
    to_visit.append([init_i, init_j])
    while to_visit:
        nodei, nodej = to_visit.popleft()
        for k in range(8):
            xi = nodei + di[k]
            xj = nodej + dj[k]
            if xi < 0 or xj < 0 or xi >= n or xj >= n:
                continue
            if matrix[xi][xj] in {".", "0"}:
                continue
            matrix[xi][xj] = "."
            to_visit.append([xi, xj])

t = 0
while True:
    t += 1
    try:
        n = int(input())
    except:
        break
    
    matrix = []
    for _ in range(n):
        matrix.append(list(input()))
    
    count = 0
    for i in range(n):
        for j in range(n):
            if matrix[i][j] in {".", "0"}:
                continue
            bfs(matrix, i, j)
            count += 1
    print(f"Image number {t} contains {count} war eagles.")
