def run_cli(graph):
    locations = list(graph.adjacency_list.keys())

    print("\n📍 Available Locations:")
    for loc in locations:
        print(f"  - {loc}")

    while True:
        start = input("\nEnter current location: ").strip()
        if start not in locations:
            print("❌ Invalid start location. Please choose from the list.")
            continue

        end = input("Enter destination location: ").strip()
        if end not in locations:
            print("❌ Invalid destination. Please choose from the list.")
            continue

        if start == end:
            print("⚠️ Start and destination cannot be the same.")
            continue

        return start, end
