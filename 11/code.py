import re


class Monkey:
    def __init__(self, items: list, stress_func, test_func):
        self.items = items
        self.stress_func = stress_func
        self.test_func = test_func
        self.inspected_item_count = 0


def stress_func_generator(operation, number):
    if operation == "*":
        return (lambda x: x * x) if "old" == number else (lambda x: x * int(number))
    elif operation == "+":
        return (lambda x: x + x) if "old" == number else (lambda x: x + int(number))


def test_func_generator(op, true_to, false_to):
    return lambda x: true_to if x % op == 0 else false_to


input = None
monkeys = []
with open("./11/input.txt") as input:
    input = input.read().splitlines()
    for i in range(0, len(input), 7):

        items = [
            int(item) for item in re.findall(r": (.*)", input[i + 1])[0].split(",")
        ]
        operation_split = re.findall(r"old (.*)", input[i + 2])[0].split(" ")
        operation, number = operation_split[0], operation_split[1]
        divisible_by = int(re.findall(r"(\d+)", input[i + 3])[0])
        true_move_to = int(re.findall(r"(\d+)", input[i + 4])[0])
        false_move_to = int(re.findall(r"(\d+)", input[i + 5])[0])

        monkey = Monkey(
            items,
            stress_func_generator(operation, number),
            test_func_generator(divisible_by, true_move_to, false_move_to),
        )

        monkeys.append(monkey)


# part 1

for i in range(10000):
    for monkey in monkeys:
        for item in list(monkey.items):
            monkey.items.remove(item)
            monkey.inspected_item_count += 1
            new_worry_level = monkey.stress_func(item) // 3
            monkeys[monkey.test_func(new_worry_level)].items.append(new_worry_level)

monkey_business_values = []
for monkey in monkeys:
    monkey_business_values.append(monkey.inspected_item_count)
largest = max(monkey_business_values)
monkey_business_values.remove(largest)
second_largest = max(monkey_business_values)
print(largest * second_largest)
