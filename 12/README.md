# Day 12: Hill Climbing Algorithm

[instructions](https://adventofcode.com/2022/day/12)

## Part One

I didn't had a lot of time to solve today's problem so I went to the simplest solution I could find, using breadth first search to find the shortest path from the starting point to the ending point.

```python
from collections import deque


class Dijkstra():
    def __init__(self,grid,start):
        self.grid = grid
        self.start = start
        self.queue = deque([(start,0)])
        self.distance = {}
        self.visited = {f"{start}": True}


    def visit_node(self):
        while(self.queue):
            (node,distance) = self.queue.popleft()
            for neighbor in self.grid[node]:
                if(
                    neighbor not in self.distance
                    or (
                        neighbor in self.distance 
                        and self.distance[neighbor] > distance + 1
                    )
                ):
                    self.distance[neighbor] = distance + 1
                if(neighbor not in self.visited):
                    self.visited[neighbor] = True
                    self.queue.append((neighbor, distance+1))
        return self.distance   


def hill_climbing():
    points = {
        "start_point": "",
        "end_point": ""
    }
    def set_height(point,x,y):
        if(point == "S"):
            points["start_point"] = f"{x}_{y}"
            return 0
        if(point == "E"):
            points["end_point"] = f"{x}_{y}"
            return 26
        return ord(point) - 96

    with open("./input") as file:
        lines = file.read().split("\n")[:-1]
        lines_x = lines
        height,width = len(lines),len(lines[0])

        lines = [set_height(char,x,y) for y,line in enumerate(lines) for x,char in enumerate(line.rstrip())]
        grid = [lines[i*width:(i+1)*width] for i in range(0,height)]
        graph = {}
        for y,row in enumerate(grid):
            for x,column in enumerate(row):
                neighbors = []
                if(0 < x and (row[x-1] - column) <= 1):
                    neighbors.append(f"{x-1}_{y}")
                if(x < width-1 and (row[x+1] - column) <= 1):
                    neighbors.append(f"{x+1}_{y}")
                if(0 < y and (grid[y-1][x] - column) <= 1):
                    neighbors.append(f"{x}_{y-1}")
                if(y < height-1 and (grid[y+1][x] - column) <= 1):
                    neighbors.append(f"{x}_{y+1}")
                graph[f"{x}_{y}"] = neighbors

        return Dijkstra(graph,points["start_point"]).visit_node()[points["end_point"]]
```

## Part Two

The quickest solution I foudn was to do the opposite of what was asked and to try and find the shortest path starting from the end point:

```python
from collections import deque

class Dijkstra():
    def __init__(self,grid,start):
        self.grid = grid
        self.start = start
        self.queue = deque([(start,0)])
        self.distance = {}
        self.visited = {f"{start}": True}


    def visit_node(self):
        while(self.queue):
            (node,distance) = self.queue.popleft()
            for neighbor in self.grid[node]:
                if(
                    neighbor not in self.distance
                    or (
                        neighbor in self.distance 
                        and self.distance[neighbor] > distance + 1
                    )
                ):
                    self.distance[neighbor] = distance + 1
                if(neighbor not in self.visited):
                    self.visited[neighbor] = True
                    self.queue.append((neighbor, distance+1))
        return self.distance   


def hill_climbing():
    points = {
        "start_points": [],
        "end_point": ""
    }
    def set_height(point,x,y):
        if(point == "a"):
            points["start_points"].append(f"{x}_{y}")
            return 1
        if(point == "E"):
            points["end_point"] = f"{x}_{y}"
            return 26
        return ord(point) - 96

    with open("./input") as file:
        lines = file.read().split("\n")[:-1]
        height,width = len(lines),len(lines[0])

        lines = [set_height(char,x,y) for y,line in enumerate(lines) for x,char in enumerate(line.rstrip())]
        grid = [lines[i*width:(i+1)*width] for i in range(0,height)]
        graph = {}
        for y,row in enumerate(grid):
            for x,column in enumerate(row):
                neighbors = []
                if(0 < x and (row[x-1] - column) >= -1):
                    neighbors.append(f"{x-1}_{y}")
                if(x < width-1 and (row[x+1] - column) >= -1):
                    neighbors.append(f"{x+1}_{y}")
                if(0 < y and (grid[y-1][x] - column) >= -1):
                    neighbors.append(f"{x}_{y-1}")
                if(y < height-1 and (grid[y+1][x] - column) >= -1):
                    neighbors.append(f"{x}_{y+1}")
                graph[f"{x}_{y}"] = neighbors

        result = Dijkstra(graph,points["end_point"]).visit_node()
        min_walk = float('inf')
        for point in result:
            if(point in points["start_points"] and result[point] < min_walk):
                min_walk = result[point]
        return min_walk
```
