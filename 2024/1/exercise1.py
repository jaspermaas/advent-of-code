import argparse

# Parse the arguments
parser = argparse.ArgumentParser()
parser.add_argument('--filename', type=str, required=True)
args = parser.parse_args()

# Load the data
with open(args.filename) as f:
    data = f.readlines()
    left = [line.strip().split()[0] for line in data]
    right = [line.strip().split()[1] for line in data]
    
left.sort()
right.sort()
distance = 0
for i in range(len(left)):
    distance += abs(int(left[i]) - int(right[i]))

print(distance)