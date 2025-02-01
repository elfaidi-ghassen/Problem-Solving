import sys, os
if os.path.exists("input.txt"):
    sys.stdin = open("input.txt")

done = False
out = []
while not done:
    n = int(input())
    graph = {}

    stack = []
    def dfs(start_node):
        
        stack.append(start_node)
        while stack:
            n = stack.pop()
            if n not in graph:
                continue
            for node in graph[n]:
                if node not in visited:
                    stack.append(node)
                    visited.add(node)


    def dfs(start_node):
        
        stack.append(start_node)
        while stack:
            n = stack.pop()
            if n not in graph:
                continue
            for node in graph[n]:
                if node not in visited:
                    stack.append(node)
                    visited.add(node)

    while True:
        try:
            line = input()
        except:
            done = True
            break
        if line == "0":
            break
        nodes = list(map(int, line.split()))
        key = nodes[0]
        if key not in graph:
            graph[key] = []
        nodes.pop(0)
        nodes.pop()
        for node in nodes:
            graph[key].append(node)
    if done:
        break
    queries = list(map(int, input().split()))
    queries.pop(0)
    nodes = set(n for n in range(1, n + 1))
    for k in queries:
        visited = set()
        if k in graph:
            dfs(k)
        result = nodes - visited
        
        if len(result) > 0:
            s = str(len(result)) + " " + " ".join(map(str, sorted(result)))
        else:
            s = str(len(result))
        out.append(s)
        visited.clear()
print("\n".join(out))