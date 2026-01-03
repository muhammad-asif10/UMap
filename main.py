from utils.loader import load_campus_map
from services.navigator import find_shortest_path
from ui.cli import run_cli
from visualization.ascii_path import draw_ascii_path
from colorama import Fore, Style

def main():
    graph = load_campus_map("data/campus_map.json")

    start, end = run_cli(graph)

    if start not in graph.adjacency_list or end not in graph.adjacency_list:
        print(Fore.RED + "❌ Invalid location entered")
        return

    path, time = find_shortest_path(graph, start, end, debug=True)

    if path:
        print(Fore.CYAN + "\n✅ Shortest Path Found:\n")
        draw_ascii_path(path)
        print(Fore.GREEN + f"\n⏱️ Estimated Time: {round(time,2)} minutes")
    else:
        print(Fore.RED + "❌ No path found")

if __name__ == "__main__":
    main()
