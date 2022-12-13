from collections import deque

def print_graph(graph):
    rows = []
    for line in graph:
        row = []
        for char in line:
            if(len(f"{char}") == 1):
                row.append(f"0{char}")
            else:
                row.append(f"{char}")
        rows.append(row)
    for row in rows:
        print(" ".join(row))


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


print(hill_climbing())