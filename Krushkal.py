class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
            return True
        return False

def kruskal(graph):
    edges = []
    for u in graph:
        for v, weight in graph[u].items():
            edges.append((weight, u, v))
    edges.sort()  
    n = len(graph)
    mst = []
    ds = DisjointSet(n)

    for weight, u, v in edges:
        if ds.union(u, v):
            mst.append((u, v, weight))

    return mst
graph = {
    'A': {'B': 2, 'D': 1},
    'B': {'A': 2, 'C': 3, 'D': 2},
    'C': {'B': 3, 'D': 1, 'E': 1},
    'D': {'A': 1, 'B': 2, 'C': 1, 'E': 3},
    'E': {'C': 1, 'D': 3}
}
mst = kruskal(graph)
print("Minimum Spanning Tree (Kruskal's algorithm):")
for u, v, weight in mst:
    print(f"{u} - {v}: {weight}")
