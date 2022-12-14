import collections


def calorie_counting_top_n(top_n=3):
    buffer = 0
    max_calorie = collections.deque([0] * top_n, top_n)

    def stack_insert(buffer):
        if buffer > max_calorie[0]:
            max_calorie.popleft()
            index = 0
            while index < top_n - 1:
                if max_calorie[index] < buffer:
                    index += 1
                else:
                    break
            max_calorie.insert(index, buffer)
        return max_calorie

    with open("./input") as file:
        for line in file:
            if line == "\n":
                stack_insert(buffer)
                buffer = 0
            else:
                buffer += int(line.rstrip())
    return sum(stack_insert(buffer))


print(calorie_counting_top_n())
