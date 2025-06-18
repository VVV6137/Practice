def components(n, e):
    graph = {i: [] for i in range(1, n + 1)}
    for u, v in e:
        graph[u].append(v)
        graph[v].append(u)
    visited = set()
    components = 0
    def dfs(node):
        stack = [node]
        while stack:
            curr = stack.pop()
            for neighbor in graph[curr]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)
    for node in range(1, n + 1):
        if node not in visited:
            components += 1
            visited.add(node)
            dfs(node)
    return components - 1

n, m = map(int, input().split())
e = [tuple(map(int, input().split())) for _ in range(m)]
print(components(n, e))
