# Project Statement: Campus Route Planner

## Problem Statement

Students, visitors, and new campus members may be unfamiliar with the paths between campus locations. When they need to get from one place to another, choosing a route by guesswork can take longer than necessary. Campus Route Planner models campus paths and their estimated walking times, then calculates a route with the lowest total estimated time between a selected start and destination.

## Scope of the Project

The project is a small Python command-line application. It includes a sample campus map represented as a weighted, undirected graph, accepts a start and destination, validates the location names, calculates a minimum-time route with Dijkstra's algorithm, and displays the route and estimated walking time.

The current version uses a fixed sample map stored in the source code. It does not include a graphical interface, live positioning, live traffic or path closures, or persistent storage. The map can be customized by changing the locations and edge weights in the program.

## Target Users

- Students navigating between campus buildings.
- Visitors who need directions between campus locations.
- New students or staff learning the campus layout.
- A course instructor evaluating graph data structures and shortest-path algorithms.

## High-Level Features

1. **View locations:** Show the locations available in the campus map.
2. **Choose route endpoints:** Take a start and destination from command-line arguments and validate them.
3. **Find a route:** Use Dijkstra's algorithm to determine a route with the lowest estimated walking time.
4. **Display directions:** Print the ordered locations in the route and the estimated total time.
5. **Handle invalid input:** Explain when a requested location is not present in the map.
