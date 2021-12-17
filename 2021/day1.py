from utils import toPath

input_path = toPath("input/day1_0")

with open(input_path) as file:
    content = file.readlines()
    content = [int(line.rstrip()) for line in content]

count1 = 0
for i in range(1, len(content)):
    if(content[i] > content[i-1]): 
        count1 += 1


print(f"Part 1: {str(count1)}")

window = 3
count2 = 0
for i in range(len(content) - window):
    sumFirst = sum(content[i: i + window])
    sumSecond = sum(content[i + 1: i + 1 + window])
    if(sumSecond > sumFirst): 
        count2 += 1

print(f"Part 2: {str(count2)}")