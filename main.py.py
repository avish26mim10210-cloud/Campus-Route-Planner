"""A small command-line campus route planner using graph algorithms."""

from __future__ import annotations

import argparse
import heapq


# Undirected weighted graph; weights represent walking minutes.
CAMPUS_MAP: dict[str, dict[str, int]] = {
    "Main Gate": {"Library": 4, "Admin Block": 3},
    "Library": {"Main Gate": 4, "Cafeteria": 2, "Science Block": 5},
    "Admin Block": {"Main Gate": 3, "Cafeteria": 4, "Sports Ground": 6},
    "Cafeteria": {"Library": 2, "Admin Block": 4, "Science Block": 3},
    "Science Block": {"Library": 5, "Cafeteria": 3, "Hostel": 4},
    "Sports Ground": {"Admin Block": 6, "Hostel": 3},
    "Hostel": {"Science Block": 4, "Sports Ground": 3},
}


def shortest_route(graph: dict[str, dict[str, int]], start: str, destination: str):
    """Return (path, total_minutes) using Dijkstra's shortest-path algorithm."""
    distances = {place: float("inf") for place in graph}
    previous: dict[str, str | None] = {place: None for place in graph}
    distances[start] = 0
    queue: list[tuple[int, str]] = [(0, start)]

    while queue:
        distance, place = heapq.heappop(queue)
        if distance != distances[place]:  # Ignore an outdated queue entry.
            continue
        if place == destination:
            break
        for neighbor, minutes in graph[place].items():
            candidate = distance + minutes
            if candidate < distances[neighbor]:
                distances[neighbor] = candidate
                previous[neighbor] = place
                heapq.heappush(queue, (candidate, neighbor))

    if distances[destination] == float("inf"):
        return None, None

    path = []
    place: str | None = destination
    while place is not None:
        path.append(place)
        place = previous[place]
    path.reverse()
    return path, int(distances[destination])


def main() -> None:
    parser = argparse.ArgumentParser(description="Find a quick walking route around campus.")
    parser.add_argument("start", nargs="?", help="starting campus location")
    parser.add_argument("destination", nargs="?", help="destination campus location")
    args = parser.parse_args()

    places = sorted(CAMPUS_MAP)
    if args.start is None or args.destination is None:
        print("Campus locations:")
        for place in places:
            print(f"  - {place}")
        print("\nUsage: python campus_routes.py \"Main Gate\" \"Hostel\"")
        return

    if args.start not in CAMPUS_MAP or args.destination not in CAMPUS_MAP:
        parser.error("unknown location; run without arguments to see the location list")

    path, minutes = shortest_route(CAMPUS_MAP, args.start, args.destination)
    if path is None:
        print(f"No route found from {args.start} to {args.destination}.")
    else:
        print("Route: " + " -> ".join(path))
        print(f"Estimated walking time: {minutes} minutes")


if __name__ == "__main__":
    main()
