from collections import deque
import sys, os
if os.path.exists("input.txt"):
    sys.stdin = open("input.txt")

n, m = map(int, input().split())
direction = {
    ">": (0, 1),
    "<": (0, -1),
    "^": (-1, 0),
    "v": (1, 0)
}
dx = input()
dy = input()

def get_nodes(i, j):
    d1 = direction[dx[i]]
    d2 = direction[dy[j]]
    nodes = []
    xi1 = i + d1[0]
    xj1 = j + d1[1]
    if xi1 >= 0 and xj1 >= 0 and xi1 < n and xj1 < m:
        nodes.append((xi1, xj1))

    xi2 = i + d2[0]
    xj2 = j + d2[1]
    if xi2 >= 0 and xj2 >= 0 and xi2 < n and xj2 < m:
        nodes.append((xi2, xj2))
        
    
    
    return nodes


def bfs_count(i, j):
    to_visit = deque()
    to_visit.append((i, j))
    visited = [[False] * m for _ in range(n)]
    count = 0
    while to_visit:
        nodei, nodej = to_visit.popleft()
        for node in get_nodes(nodei, nodej): 
            xi, xj = node
            if visited[xi][xj]:
                continue
            to_visit.append(node)
            visited[xi][xj] = True
            count += 1
    return count
        
for i in range(n):
    for j in range(m):
        if bfs_count(i, j) < n * m:
            print("NO")
            sys.exit()
print("YES")