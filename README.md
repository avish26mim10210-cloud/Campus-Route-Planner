# Campus Route Planner

## Overview

Campus Route Planner is a command-line program that finds a minimum-time walking route between two locations on a sample campus. It models locations and walking paths as a weighted graph and uses Dijkstra's algorithm to calculate the route.

## Features

- Lists the available campus locations.
- Accepts a starting point and destination from the command line.
- Calculates and displays a minimum-time route and estimated walking time.
- Reports an error when a location name is not in the map.
- Uses a sample campus map that can be replaced with locations and times from your campus.

## Technologies and Tools Used

- Python 3.10 or newer
- Python standard library: `argparse` and `heapq`
- Weighted graph represented by nested dictionaries
- Dijkstra's shortest-path algorithm

## Installation and Run Steps

1. Install Python 3.10 or newer.
2. Download or clone this project and open a terminal in the `campus-route-planner` folder.
3. List available locations:

   ```text
   python campus_routes.py
   ```

4. Find a route (use quotes around location names containing spaces):

   ```text
   python campus_routes.py "Main Gate" "Hostel"
   ```

Example output:

```text
Route: Main Gate -> Library -> Science Block -> Hostel
Estimated walking time: 13 minutes
```

## Testing Instructions

This version does not include automated tests. To check it manually:

- Run the program without arguments and confirm that it lists the locations and usage.
- Request a route between two known places and confirm that the route and time are printed.
- Try an unknown place and confirm that the program reports an input error.
- Use the same known place as both start and destination and confirm that the route time is zero.

## Screenshots

No screenshots are included yet. Add a terminal screenshot here after running the program, for example:

```markdown
![Route planner output](screenshots/route-example.png)
```

## Project Files

```text
campus-route-planner/
├── campus_routes.py   # Campus graph, route calculation, and command-line interface
├── README.md          # Project overview and usage guide
└── statement.md       # Problem statement, scope, users, and high-level features
```

## Algorithm

The campus is stored as a weighted, undirected graph. Locations are vertices; connections are edges weighted by estimated walking minutes. Dijkstra's algorithm uses a priority queue to find the route with the lowest total time. With a binary heap, its typical time complexity is `O((V + E) log V)`, where `V` is the number of locations and `E` is the number of connections.

The included map is sample data. Replace its locations and estimated times with information relevant to your campus, and make sure you can explain the implementation and algorithm for your course submission.
