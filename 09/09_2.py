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


print(rope_bridge(), rope_bridge()==2369)