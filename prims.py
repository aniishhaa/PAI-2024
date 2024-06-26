import heapq

def prim(graph):
    min_heap = [(0, list(graph.keys())[0])]  
    mst = set()
    total_cost = 0

    while min_heap:
        cost, node = heapq.heappop(min_heap)
        if node not in mst:
            mst.add(node)
            total_cost += cost
            for neighbor, weight in graph[node].items():
                if neighbor not in mst:
                    heapq.heappush(min_heap, (weight, neighbor))

    return total_cost
graph = {
    'A': {'B': 2, 'D': 1},
    'B': {'A': 2, 'C': 3, 'D': 2},
    'C': {'B': 3, 'D': 1, 'E': 1},
    'D': {'A': 1, 'B': 2, 'C': 1, 'E': 3},
    'E': {'C': 1, 'D': 3}
}
mst_cost = prim(graph)
print(f"Minimum Spanning Tree cost (Prim's algorithm): {mst_cost}")
