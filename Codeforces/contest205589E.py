import sys, os 
from collections import deque

if os.path.exists("input.txt"): 
    sys.stdin = open("input.txt") 

_ = input()
c, r = map(int, input().split())
_ = input()



matrix = []
for _ in range(r):
    line = list(map(int, input().split()))
    matrix.append(line)

visited = [[False] * c for _ in range(r)] 
w = 0
b = 0

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def bfs(i, j):
    to_visit = deque([(i, j)])
    visited[i][j] = True
    color = matrix[i][j]
    while to_visit:
        first = to_visit.popleft()
        for i in range(4):
            x, y = first
            x += dx[i]
            y += dy[i]
            if (x < 0 or y < 0 or x > r - 1 or y > c - 1 or visited[x][y] or matrix[x][y] != color):
                continue
            to_visit.append((x, y))
            visited[x][y] = True



for i in range(r):
    for j in range(c):
        if visited[i][j]:
            continue
        if matrix[i][j] == 255:
            w += 1
        if matrix[i][j] == 0:
            b += 1
        bfs(i, j)

wp = b // 4
android = (w - 1) // 2
wp = wp - android

if (wp == android):
    print("Tie")
elif wp > android:
    print("Hasan")
else:
    print("Bahosain")
print(wp, android)