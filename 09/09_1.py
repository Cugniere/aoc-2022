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


print(rope_bridge(), rope_bridge() == 6266)
