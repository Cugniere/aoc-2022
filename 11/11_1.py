import math
import re


class Monkey:
    def __init__(self, raw_params):
        parameters = raw_params.split("\n")
        self.items = [
            int(item) for item in parameters[1].lstrip("Starting items:").split(", ")
        ]
        self.multiply = re.match(".*(\+|\*)", parameters[2])[1] == "*"
        self.target_self = len(re.findall("(old)", parameters[2])) == 2
        if not self.target_self:
            self.factor = int(re.search("\d+", parameters[2])[0])
        self.condition_divisor = int(re.search("\d+", parameters[3])[0])
        self.condition_valid_target = int(re.search("\d+", parameters[4])[0])
        self.condition_invalid_target = int(re.search("\d+", parameters[5])[0])
        self.active = 0

    def join_group(self, monkeys):
        self.monkeys = monkeys

    def inspect(self):
        for item in self.items:
            self.active += 1
            if self.target_self and self.multiply:
                self.throw(item * item)
            elif self.target_self and not self.multiply:
                self.throw(item + item)
            elif not self.target_self and self.multiply:
                self.throw(item * self.factor)
            else:
                self.throw(item + self.factor)
        self.items = []

    def throw(self, item):
        item = math.floor(item / 3)
        if (item % self.condition_divisor) == 0:
            target = self.condition_valid_target
        else:
            target = self.condition_invalid_target
        self.monkeys[target].items.append(item)



def monkey_in_the_middle(limit=20):
    with open("./input") as file:
        monkeys = [Monkey(monkey) for monkey in file.read().split("\n\n")]
        [monkey.join_group(monkeys) for monkey in monkeys]
        for round in range(limit):
            for monkey in monkeys:
                monkey.inspect()
    return math.prod(sorted([monkey.active for monkey in monkeys])[-2:])


print(monkey_in_the_middle(), monkey_in_the_middle() == 55930)
