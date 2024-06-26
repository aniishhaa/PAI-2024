import heapq

def dijkstra(graph, start):
    min_heap = [(0, start)]  
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    path = {}

    while min_heap:
        current_distance, current_node = heapq.heappop(min_heap)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                path[neighbor] = current_node
                heapq.heappush(min_heap, (distance, neighbor))

    return distances, path

graph = {
    'A': {'B': 2, 'C': 4},
    'B': {'A': 2, 'C': 1, 'D': 7},
    'C': {'A': 4, 'B': 1, 'D': 3},
    'D': {'B': 7, 'C': 3}
}
start_node = 'A'
distances, path = dijkstra(graph, start_node)

print(f"Shortest paths from node '{start_node}':")
for node in graph:
    if node != start_node:
        path_str = f"{node} → "
        current_node = node
        while current_node in path:
            path_str += f"{path[current_node]} → "
            current_node = path[current_node]
        path_str += start_node
        print(f"{path_str}: {distances[node]}")
