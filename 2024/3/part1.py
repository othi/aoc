import re

with open("input") as f:
    input = "".join(f.read().split("\n"))


matches = re.findall("mul\(\d+,\d+\)", input)

result = 0
for match in matches:
    match = match[4:]
    result += int(match[: match.find(",")]) * int(match[match.find(",") + 1 : -1])

print(result)
