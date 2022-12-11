def cpu_instructions(width=40, height=6):
    def draw_pixel(value, cycle, screen):
        position = (cycle - 1) % width
        if position in {value - 1, value, value + 1}:
            screen[cycle - 1] = "#"

    with open("./input") as file:
        screen = ["."] * (width * height)

        value = 1
        cycle = 0
        for line in file:
            cycle += 1
            draw_pixel(value, cycle, screen)
            if line.rstrip() != "noop":
                cycle += 1
                draw_pixel(value, cycle, screen)
                value += int(line.rstrip().split(" ")[1])

        for line in [
            screen[index : index + width] for index in range(0, len(screen), width)
        ]:
            print("".join(line))


cpu_instructions()
