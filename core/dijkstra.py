import heapq

def dijkstra(graph, start, debug=False):
    distances = {node: float('inf') for node in graph.adjacency_list}
    previous = {}
    distances[start] = 0

    pq = [(0, start)]

    if debug:
        print("\n[DEBUG] Starting Dijkstra from:", start)

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if debug:
            print(f"[DEBUG] Visiting {current_node} (distance = {current_distance})")

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph.get_neighbors(current_node):
            new_distance = current_distance + weight

            if debug:
                print(f"  → Checking {neighbor} via {current_node} (cost = {new_distance})")

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = current_node
                heapq.heappush(pq, (new_distance, neighbor))

                if debug:
                    print(f"    ✔ Updated shortest path to {neighbor}")

    return distances, previous
