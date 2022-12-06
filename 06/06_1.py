def tuning_trouble(signal_length):
    with open("./input") as file:
        line = file.read()
        for index in range(len(line) - signal_length):
            if len(set(line[index : index + signal_length])) == signal_length:
                return index + signal_length


print(tuning_trouble(4))
