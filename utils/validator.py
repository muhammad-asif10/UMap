def validate_location(graph, location):
    if location not in graph.adjacency_list:
        raise ValueError(f"❌ Invalid location: '{location}'")

def validate_same_location(start, end):
    if start == end:
        raise ValueError("❌ Start and destination cannot be the same")
