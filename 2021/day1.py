from utils import toPath

input_path = toPath("input/day1_0")

with open(input_path) as file:
    content = file.readlines()
    content = [int(line.rstrip()) for line in content]

count = 0
for i in range(1, len(content)):
    if(content[i] > content[i-1]): 
        count += 1

print("Day 1")
print(count)