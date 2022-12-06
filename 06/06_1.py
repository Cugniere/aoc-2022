import collections


def tuning_trouble(signal_length):
    buffer = collections.deque()
    with open("./input") as file:
        line = file.read()
        for index, char in enumerate(line):
            buffer.append(char)
            if len(buffer) == signal_length:
                if len(set(buffer)) == signal_length:
                    return index + 1
                buffer.popleft()


print(tuning_trouble(4))
