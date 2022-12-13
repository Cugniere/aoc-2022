# Day 9: Rope Bridge

[instructions](https://adventofcode.com/2022/day/9)

## Part One

Today's problem doesn't require a lot of coding skill but some basic logical understanding. Both a notebook and a visualization function can be of great help to find the solution.

Here's my code for the first part:
```python
def rope_bridge():
    tail_x,tail_y,head_x,head_y = 0,0,0,0
    with open("./input") as file:
        covered_cells = {"0_0": 1}
        for line in file:
            direction, movements = line.rstrip().split(" ")
            if direction == "R":
                head_x = head_x + int(movements)
            elif direction == "L":
                head_x = head_x - int(movements)
            elif direction == "U":
                head_y = head_y + int(movements)
            elif direction == "D":
                head_y = head_y - int(movements)

            while (
                (abs(head_x - tail_x) + abs(head_y - tail_y)) / 2 > 1
                or abs(head_x - tail_x) > 1
                or abs(head_y - tail_y) > 1
            ):
                if head_x - tail_x > 0:
                    tail_x += 1
                elif head_x - tail_x < 0:
                    tail_x += -1
                if head_y - tail_y > 0:
                    tail_y += 1
                elif head_y - tail_y < 0:
                    tail_y += -1

                covered_cells[f"{tail_x}_{tail_y}"] = True
                
        return sum([visited_count for visited_count in covered_cells.values()])
```
Basically we read the file line by line and move the "head" instantly from one point to another. Then, we move the tail using the shortest path (either in diagonal or in a straight line/column), always keeping to the tile previously occupied by the tail. I used a dictionnary (`covered_cells`) as a way to keep track of every visited cells.

## Part Two

As I expected my code isn't reusable from scratch. The main problem here is that each knot on the rope can move in a different direction and will try to move in the shortest way possible relatively to the previous knot. However, the whole rope doesn't move in a straight line.

Here's my code:
```python
def rope_bridge(rope_size=9):
    head_x,head_y = 0,0
    rope_knots = []
    for knot in range(rope_size):
        rope_knots.append({"x": 0, "y": 0})
    covered_cells = {"0_0": True}
    with open("./input") as file:    
        for line in file:
            direction,movements = line.rstrip().split(" ")
            target_x,target_y = head_x,head_y
            if(direction == "R"):
                target_x = head_x+int(movements)
            elif(direction == "L"):
                target_x = head_x-int(movements)
            elif(direction == "U"):
                target_y = head_y+int(movements)
            elif(direction == "D"):
                target_y = head_y-int(movements)

            while(head_x != target_x or head_y != target_y):
                if(head_x < target_x):
                    head_x += 1
                elif(head_x > target_x):
                    head_x -= 1
                if(head_y < target_y):
                    head_y += 1
                elif(head_y > target_y):
                    head_y -= 1

                for index,knot in enumerate(rope_knots):
                    if(index == 0):
                        knot_head_x = head_x
                        knot_head_y = head_y
                    else:
                        knot_head_x = rope_knots[index-1]["x"]
                        knot_head_y = rope_knots[index-1]["y"]
                    while(
                        (abs(knot_head_x - knot["x"]) + abs(knot_head_y - knot["y"]))/2 > 1
                        or abs(knot_head_x - knot["x"]) > 1
                        or abs(knot_head_y - knot["y"]) > 1
                        ):
                        if(knot_head_x - knot["x"] > 0):
                            knot["x"] += 1
                        elif(knot_head_x - knot["x"] < 0):
                            knot["x"] += -1
                        if(knot_head_y - knot["y"] > 0):
                            knot["y"] += 1
                        elif(knot_head_y - knot["y"] < 0):
                            knot["y"] += -1
                        if(index == rope_size-1):
                            covered_cells[f"{knot['x']}_{knot['y']}"] = True

        return sum([visited_count for visited_count in covered_cells.values()])
```
The main change here is that each time the head move, we need to calculate its position one tile at time in order to update the position of the knots correctly. Also, each knot position is computed relatively to the previous knot.
