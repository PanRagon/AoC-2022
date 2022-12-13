import math
import operator
from functools import reduce
from test import test_input

from input import input

#Setup
monkeys = input.split('\n\n')


class Monkey:
    def __init__(self, name, starting_items, operation, divisor, success_monkey, fail_money):
        self.name = name
        self.items = starting_items
        self.divisor = divisor
        self.success_monkey = success_monkey
        self.fail_monkey = fail_money
        self.inspections = 0
        #Could use lambda?
        self.operation = lambda item : eval(f"{item} {operation[1]} {int(operation[2]) if operation[2].isnumeric() else item}")

    def __str__(self):
        return f"Monkey {self.name}:"
    
    def recieve_item(self, item):
        self.items.append(item)
    
    def throw_item(self, item):
        self.items.remove(item)

    def reset_monkey(self):
        self.inspections = 0
        self.items = []

    def inspect(self):
        self.inspections += 1
        self.items[0] = int(self.operation(self.items[0]))
        self.items[0] = int(self.items[0] / 3)
        if(self.items[0] % int(self.divisor) == 0):
            monkey_list[self.success_monkey].recieve_item(self.items[0])
        else:
            monkey_list[self.fail_monkey].recieve_item(self.items[0])
        self.throw_item(self.items[0])
    def inspect_with_massive_worry(self, mod):
        self.inspections += 1
        self.items[0] = int(self.operation(self.items[0]))
        self.items[0] = self.items[0] % mod
        if(self.items[0] % int(self.divisor) == 0):
            monkey_list[self.success_monkey].recieve_item(self.items[0])
        else:
            monkey_list[self.fail_monkey].recieve_item(self.items[0])
        self.throw_item(self.items[0])

monkey_list = []
lcm = 1
def generate_monkeys():
    for idx, monkey in enumerate(monkeys):
        monkey_attributes = monkey.split('\n')
        monkey_name = monkey_attributes[0].split(':')[0].split(' ')[1]
        monkey_starting_items = monkey_attributes[1].split(':')[1].split(',')
        monkey_operation = monkey_attributes[2].split('=')[1].split()
        monkey_divisor = monkey_attributes[3].split()[-1]
        monkey_success_monkey = int(monkey_attributes[4].split()[-1])
        monkey_fail_monkey = int(monkey_attributes[5].split()[-1])
        monkey_list.append(Monkey(monkey_name, monkey_starting_items, monkey_operation, monkey_divisor, monkey_success_monkey, monkey_fail_monkey))
    return reduce(operator.mul, [int(m.divisor) for m in monkey_list])
#Run
def play_rounds(rounds):
    for i in range(rounds):
        for monkey in monkey_list:
            while(len(monkey.items) > 0):
                monkey.inspect()
def get_most_inspections(n=2):
    return sorted(monkey_list, key=lambda monkey: monkey.inspections)[-n:]

#Part 1:
lcm = generate_monkeys()
play_rounds(20)
for monkey in monkey_list:
    print(monkey.name, "has inspected: ", monkey.inspections)
most = get_most_inspections(2)
#Solution part 1:
print('Solution to part 1: ', most[0].inspections * most[1].inspections)

monkey_list = []
#Part 2:
lcm = generate_monkeys()
print(lcm)
def play_rounds_with_worry(rounds):
    for i in range(rounds):
        for monkey in monkey_list:
            while(len(monkey.items) > 0):
                monkey.inspect_with_massive_worry(lcm)

play_rounds_with_worry(10000)
most_monkey_business = get_most_inspections(2)
print('Solution part 2 : ', most_monkey_business[0].inspections * most_monkey_business[1].inspections)