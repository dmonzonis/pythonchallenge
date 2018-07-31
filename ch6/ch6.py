import pickle

# Load pickled data
with open("peakhell.p", 'rb') as f:
    data = pickle.load(f)

# Print secret message
for line in data:
    for pair in line:
        print(pair[0] * pair[1], end='')
    print()
