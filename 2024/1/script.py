col1: list[int] = []
col2: list[int] = []

with open("input") as f:
    for line in f.readlines():
        tokens = line.split()
        col1.append(int(tokens[0]))
        col2.append(int(tokens[1]))

col1 = sorted(col1)
col2 = sorted(col2)

sum = 0
for i in range(len(col1)):
    sum += abs(col1[i] - col2[i])

print(sum)
