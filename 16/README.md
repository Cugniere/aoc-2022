# Day 16: Proboscidea Volcanium

[instructions](https://adventofcode.com/2022/day/16)

## Part One

Today's first part of the problem requires to traval around a weighted graph and find the optimal path to release as much pressure as possible. The task itself wasn't too hard but I worked a bit to optimize it:
- we can pre-compute the distance of the current node to all the others
- we can skip the node where there is no steam to release
- we can simplify the code by adding `1` to the distance to each node since it takes exactly one turn to open a valve

Here's my code; I use BFS to find the shortest path between 2 nodes and test all the possibles pathsince we can't be sure that going to the nearest node will give us the best release output.

```python
import re
import collections

def shortest_path(graph, start):
  queue = collections.deque([(start,1)])
  distances = {}
  visited = []
  while queue:
    node,walked = queue.popleft()
    for tunnel in graph[node]["tunnels"]:
      if(tunnel not in distances or distances[tunnel] > walked+1):
        distances[tunnel] = walked + 1
      if(tunnel not in visited):
        visited.append(tunnel)
        queue.append((tunnel, walked+1))
  return distances

def find_optimal_path(graph, start, remaining, released, visited):
  candidates = [node for node in graph[start]["paths"] if node not in visited and graph[start]["paths"][node] <= remaining]
  if(not len(candidates) or remaining <= 0):
    return released
  path_release = []
  for candidate in candidates:
    candidate_remaining = remaining - graph[start]["paths"][candidate]
    candidate_released = released + (candidate_remaining * graph[candidate]["flow"])
    path_release.append(find_optimal_path(
      graph, candidate, candidate_remaining, candidate_released, visited + [candidate]
    ))
  return max(path_release)

def optimal_pressure_release():
  with open("./input") as file:
    graph = {}
    for line in file:
      result = re.findall(r"\b([A-Z]{2}|\d{1,2})\b", line)
      if(len(result)):
        graph[result[0]] = {
          "flow": int(result[1]),
          "tunnels": result[2:]
        }
    for node in graph:
      graph[node]["paths"] = {k:v for k,v in shortest_path(graph, node).items() if graph[k]["flow"] > 0 and node != k}
    return find_optimal_path(graph, "AA", 30, 0, [next(iter(graph))])
```

## Part Two
