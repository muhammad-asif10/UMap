from core.dijkstra import dijkstra

def find_shortest_path(graph, start, end, debug=False):
    distances, previous = dijkstra(graph, start, debug)

    path = []
    current = end

    while current:
        path.insert(0, current)
        current = previous.get(current)

    if path[0] == start:
        return path, distances[end]

    return None, float('inf')
