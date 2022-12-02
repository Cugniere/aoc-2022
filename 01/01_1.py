def calorie_counting():
    buffer, max_calorie = 0, 0
    with open("./input") as file:
        for line in file:
            if line == "\n":
                max_calorie = max(max_calorie, buffer)
                buffer = 0
            else:
                buffer += int(line.rstrip("\n"))
    return buffer if buffer > max_calorie else max_calorie


print(calorie_counting())
