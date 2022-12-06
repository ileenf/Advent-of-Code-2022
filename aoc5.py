from collections import defaultdict

def supply_stack(path):
    stacks = defaultdict(list)
    commands = []

    with open(path) as file:
        for line in file:
            line = line.rstrip()

            if 'move' in line:
                line = line.strip().split()
                command = [line[1], line[3], line[5]]
                commands.append(command)

            elif '1' in line:
                continue
            else:
                stack_num = 1
                for i in range(1, len(line), 4):
                    crate = line[i]
                    if crate != ' ':
                        stacks[stack_num].append(crate)
                    stack_num += 1

    for num, stack in stacks.items():
        stacks[num] = stack[::-1]

    for amount, from_stack, to_stack in commands:
        from_stack = int(from_stack)
        to_stack = int(to_stack)

        for i in range(int(amount)):
            crate = stacks[from_stack].pop()
            stacks[to_stack].append(crate)

    stacks_in_order = sorted(stacks.items())

    crates = ''
    for num, stack in stacks_in_order:
        crates += stack[-1]
    return crates

def supply_stack2(path):
    stacks = defaultdict(list)
    commands = []

    with open(path) as file:
        for line in file:
            line = line.rstrip()

            if 'move' in line:
                line = line.strip().split()
                command = [line[1], line[3], line[5]]
                commands.append(command)

            elif '1' in line:
                continue
            else:
                stack_num = 1
                for i in range(1, len(line), 4):
                    crate = line[i]
                    if crate != ' ':
                        stacks[stack_num].append(crate)
                    stack_num += 1

    for num, stack in stacks.items():
        stacks[num] = stack[::-1]

    for amount, from_stack, to_stack in commands:
        from_stack = int(from_stack)
        to_stack = int(to_stack)

        crates_in_order = []
        for i in range(int(amount)):
            crate = stacks[from_stack].pop()
            crates_in_order.append(crate)

        for crate in crates_in_order[::-1]:
            stacks[to_stack].append(crate)

    stacks_in_order = sorted(stacks.items())

    crates = ''
    for num, stack in stacks_in_order:
        crates += stack[-1]
    return crates


print(supply_stack2('aoc5.txt'))