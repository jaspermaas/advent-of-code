import argparse

# Parse the arguments
parser = argparse.ArgumentParser()
parser.add_argument('--filename', type=str, required=True)
args = parser.parse_args()

# Load the data
with open(args.filename) as f:
    data = f.readlines()
    data = [[int(x) for x in line.strip().split()] for line in data]


def check_safety(line:list[list[int]]) -> bool:
    decreasing = False
    increasing = False
    for j in range(1, len(data[i])):
        if abs(data[i][j] - data[i][j-1]) < 1 or abs(data[i][j] - data[i][j-1]) > 3:
            return False
        if data[i][j] < data[i][j-1]:
            decreasing = True
        if data[i][j] > data[i][j-1]:
            increasing = True
        if decreasing and increasing:
            return False
    return True

sum = 0
for i in range(len(data)):
    if check_safety(data[i]):
        sum += 1
    else:
        for j in range(len(data[i])):
            # remove the element on pos j
            temp = data[i].pop(j)
            if check_safety(data[i]):
                sum += 1
                break
            data[i].insert(j, temp)

print(sum)