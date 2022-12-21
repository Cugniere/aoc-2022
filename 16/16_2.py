import re
import collections
from itertools import combinations 
import math

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
    candidates = []
    for node in graph:
      graph[node]["paths"] = {k:v for k,v in shortest_path(graph, node).items() if graph[k]["flow"] > 0 and node != k}
      if(graph[node]["flow"] > 0):
        candidates.append(node)
    
    best_candidates = 0
    for index in range(math.ceil(len(candidates)/2)+1):
      path_combinations = combinations(candidates, index)
      for nodes in path_combinations:
        elf_nodes = list(nodes)
        elephant_nodes = [node for node in candidates if node not in elf_nodes]
        elf = find_optimal_path(graph, "AA", 26, 0, ["AA"]+elf_nodes)
        elephant = find_optimal_path(graph, "AA", 26, 0, ["AA"]+elephant_nodes)
        best_candidates = max(best_candidates, elf+elephant)
    return best_candidates

print(optimal_pressure_release())

