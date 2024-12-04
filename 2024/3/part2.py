import re

with open("input") as f:
    input = "".join(f.read().split("\n"))


matches = re.findall("(mul\(\d+,\d+\))|(do(?:n't){0,1}\(\))", input)

result = 0
enabled = True
for match in matches:
    instruction = match[0] or match[1]
    if instruction == "do()":
        enabled = True
        continue
    elif instruction == "don't()":
        enabled = False
        continue
    if enabled:
        match = instruction[4:]
        result += int(match[: match.find(",")]) * int(match[match.find(",") + 1 : -1])

print(result)
