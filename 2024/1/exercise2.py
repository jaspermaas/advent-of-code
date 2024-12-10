import pandas as pd
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

similarity = 0
for i in range(len(left)):
    similarity += int(left[i]) * right.count(left[i])

print(similarity)


