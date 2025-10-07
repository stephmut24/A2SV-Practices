# Problem: Dijkstra? - https://codeforces.com/problemset/problem/20/C

from collections import defaultdict
import heapq

V, E = map(int, input().split())

graph = defaultdict(list)

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

distances = [float('inf')] * (V + 1)
parent = [-1] * (V + 1)

distances[1] = 0

pq = [(0, 1)]

while pq:
    d, u = heapq.heappop(pq)
    if d > distances[u]:
        continue
    
    for v, w in graph[u]:
        if distances[u] + w < distances[v]:
            distances[v] = distances[u] + w
            parent[v] = u
            heapq.heappush(pq, (distances[v], v))


if distances[V] == float('inf'):
    print(-1)
else:
    path = []
    cur = V


    while cur != -1:
        path.append(cur)
        cur = parent[cur]

    
    path.reverse()
    print(*path)