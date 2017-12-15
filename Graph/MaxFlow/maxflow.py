import copy
from collections import deque


def hasPath(Gf, s, t, path):
    # BFS algorithm
    V = len(Gf)
    visited = list(range(V))
    for i in range(V):
        visited[i] = False
    visited[s] = True
    queue = deque([s])
    while queue:
        temp = queue.popleft()
        if temp == t:
            return True
        print("temp =", temp)
        for i in range(V):
            if not visited[i] and (Gf[temp][i] > 0):
                queue.append(i)
                visited[i] = True
                path[i] = temp   # record precursor
    return visited[t]


def max_flow(graph, s, t):
    maxFlow = 0
    Gf = copy.deepcopy(graph)
    V = len(Gf)
    path = list(range(V))
    while hasPath(Gf, s, t, path):
        min_flow = float('inf')

        # find cf(p)
        v = t
        while v != s:
            u = path[v]
            min_flow = min(min_flow, Gf[u][v])
            v = path[v]
        print(min_flow)

        # add flow in every edge of the augument path
        v = t
        while v != s:
            u = path[v]
            Gf[u][v] -= min_flow
            Gf[v][u] += min_flow
            v = path[v]

        maxFlow += min_flow
    return maxFlow

M=0
capacity = [
[0,16,13,M,M,M],
[M,0,10,12,M,M],
[M,4,0,M,14,M],
[M,M,9,0,M,20],
[M,M,M,7,0,4],
[M,M,M,M,M,0]
]

flow = max_flow(capacity, 0, 5)
print("flow =", flow)

