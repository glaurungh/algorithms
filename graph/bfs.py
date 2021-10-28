from collections import deque

G = {
     0 : {1, 10, 11, 12},
     1 : {0, 7},
     2 : {6},
     3 : {11},
     4 : {6, 10},
     5 : {8, 13},
     6 : {2, 10, 4},
     7 : {1, 13},
     8 : {12, 5},
     9 : {11},
     10 : {6, 4, 0},
     11 : {0, 12, 9, 3, 14},
     12 : {0, 11, 8},
     13 : {7, 5},
     14 : {11}
    }

graph = G
distances = {}#[None] * len(G)
parents = {}
start_vertex = 0
distances[start_vertex] = 0
parents[start_vertex] = None
queue = deque([start_vertex])

while queue:
    vertex = queue.popleft()
    for neighbour in graph[vertex]:
        if neighbour not in distances:
            distances[neighbour] = distances[vertex] + 1
            parents[neighbour] = vertex
            queue.append(neighbour)

print(G)
print(distances)
print(parents)

start_vertex = 0
end_vertex = 9
vertex = end_vertex
