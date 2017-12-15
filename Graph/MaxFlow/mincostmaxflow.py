import copy
from heapq import *
# 最小堆

def hasPath(Gf, s, t):
    # Dijkstra algorithm using "heapq"
    V = len(Gf)
    visited = list(range(V))
    for i in range(V):
        visited[i] = False
    h = [(0, s, list(range(V)))]
    while h:
        (cost, v1, path) = heappop(h)
        if visited[v1] is False:
            visited[v1] = True
            if v1 == t:
                return True, path
            for i in range(V):
                if not visited[i] and (Gf[v1][i][0] > 0):
                    path[i] = v1   # record precursor
                    heappush(h, (cost + Gf[v1][i][1], i, copy.deepcopy(path))) # 必须要深拷贝，不然heap里的各个path都会随之改变
    return visited[t], path


def max_flow(graph, s, t):
    maxFlow = 0
    minCost = 0
    Gf = copy.deepcopy(graph)
    V = len(Gf)
    path = list(range(V))
    while hasPath(Gf, s, t)[0]:
        path = hasPath(Gf, s, t)[1]
        print("path =", path)
        min_flow = float('inf')

        # find cf(p)
        v = t
        while v != s:
            u = path[v]
            min_flow = min(min_flow, Gf[u][v][0])
            v = path[v]
        print("min_flow =", min_flow)

        # add flow in every edge of the augument path
        v = t
        while v != s:
            u = path[v]
            Gf[u][v][0] = Gf[u][v][0] - min_flow
            Gf[v][u][0] = Gf[v][u][0] + min_flow
            Gf[v][u][1] = Gf[u][v][1]
            minCost = minCost + min_flow * Gf[u][v][1]
            v = path[v]
        maxFlow += min_flow
        path = list(range(V))
    return maxFlow, minCost

capacity = [
[[0,0],[16,1],[13,3],[0,0],[0,0],[0,0]],
[[0,0],[0,0],[10,1],[12,4],[0,0],[0,0]],
[[0,0],[10,1],[0,0],[9,4],[10,2],[0,0]],
[[0,0],[0,0],[9,4],[0,0],[0,0],[20,2]],
[[0,0],[0,0],[0,0],[7,1],[0,0],[4,2]],
[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
]

flow, cost = max_flow(capacity, 0, 5)
print("\nflow =", flow)

print("cost =", cost)
