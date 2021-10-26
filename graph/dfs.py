def dfs(vertex, G, used = None):
    used = used or set()
    used.add(vertex)
    for neighbour in G[vertex]:
        if neighbour not in used:
            dfs(neighbour, G, used)

