def cpu_instructions():
    with open("./input") as file:
        signal_strengths = []
        value = 1
        cycle = 0
        for line in file:
            cycle += 1
            if (cycle - 20) % 40 == 0 and cycle <= 220:
                signal_strengths.append(cycle * value)
            if line.rstrip() != "noop":
                cycle += 1
                if (cycle - 20) % 40 == 0 and cycle <= 220:
                    signal_strengths.append(cycle * value)
                value += int(line.rstrip().split(" ")[1])
        return sum(signal_strengths)


print(cpu_instructions())
