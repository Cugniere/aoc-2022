def regolith_reservoir():
    width = 800
    height = 800
    sand_filling_point = 500
    
    rock_grid = [["."] * width for i in range(height)]
    with open("./input") as file:
        for line in file:
            couples = [(int(couple.split(",")[0]),int(couple.split(",")[1])) for couple in line.rstrip().split(" -> ")]
            for i in range(len(couples)-1):
                if(couples[i][0] < couples[i+1][0] or couples[i][1] < couples[i+1][1]):
                    (from_x,from_y),(to_x,to_y) = couples[i],couples[i+1]
                else:
                    (to_x,to_y),(from_x,from_y) = couples[i],couples[i+1]
                if(from_x < to_x):
                    for cell in range(to_x-from_x+1):
                        rock_grid[from_y][from_x+cell] = "#"
                else:
                    for cell in range(to_y-from_y+1):
                        rock_grid[from_y+cell][from_x] = "#"

        rock_grid[0][sand_filling_point] = "+"
        sand_units = 0
        sand_x,sand_y= sand_filling_point,0
        while(True):
            if(sand_x < 0 or sand_x >= width or sand_y >= height-1):
                return sand_units
            elif(rock_grid[sand_y+1][sand_x] == "."):
                sand_y+=1
            elif(rock_grid[sand_y+1][sand_x-1] == "."):
                sand_x -= 1
                sand_y += 1
            elif(rock_grid[sand_y+1][sand_x+1] == "."):
                sand_x += 1
                sand_y += 1
            else:
                sand_units +=1
                rock_grid[sand_y][sand_x] = "o"
                sand_x,sand_y= sand_filling_point,0

print(regolith_reservoir())