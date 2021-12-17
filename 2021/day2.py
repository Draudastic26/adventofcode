from utils import toPath

input_path = toPath("input/day2_0")

with open(input_path) as file:
    input = file.readlines()
    input = [line.rstrip() for line in input]

horizontal = 0
depth = 0

for command in input:
    split = command.split()
    direction = split[0]
    amount = int(split[1])
    if(direction == 'forward'):
        horizontal += amount
    elif(direction == 'down'):
        depth += amount
    elif(direction == 'up'):
        depth -= amount

print("Part 1: " + str(horizontal * depth))

horizontal = 0
depth = 0
aim = 0

for command in input:
    split = command.split()
    direction = split[0]
    amount = int(split[1])
    if(direction == 'forward'):
        horizontal += amount
        depth += aim * amount
    elif(direction == 'down'):
        aim += amount
    elif(direction == 'up'):
        aim -= amount

print("Part 2: " + str(horizontal * depth))