import argparse

# Parse the arguments
parser = argparse.ArgumentParser()
parser.add_argument('--filename', type=str, required=True)
args = parser.parse_args()

# Load the data
with open(args.filename) as f:
    data = f.readlines()
    data = [list(line.strip()) for line in data]
    data = [[int(x) for x in line] for line in data]

def find_nines(data, i, j, nines):
    if data[i][j] == 9:
        nines.append(i * len(data) + j)
    else:
        if i > 0 and data[i-1][j] == data[i][j] + 1:
            find_nines(data, i-1, j, nines)
        if i < len(data) - 1 and data[i+1][j] == data[i][j] + 1:
            find_nines(data, i+1, j, nines)
        if j > 0 and data[i][j-1] == data[i][j] + 1:
            find_nines(data, i, j-1, nines)
        if j < len(data[i]) - 1 and data[i][j+1] == data[i][j] + 1:
            find_nines(data, i, j+1, nines)
        return nines

sum = 0
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == 0:
            sum += len(find_nines(data, i, j, []))
            
print(sum)