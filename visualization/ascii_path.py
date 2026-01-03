def draw_ascii_path(path):
    print("\n📍 Path Visualization:\n")
    for i, place in enumerate(path):
        if i == len(path) - 1:
            print(f"[{place}]")
        else:
            print(f"[{place}]")
            print("   |")
            print("   v")
