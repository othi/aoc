with open("input") as f:
    input = f.readlines()


def check(y: int, x: int, currchar: str, dir: int):
    if dir == 0:  # horizontal right
        x = x + 1
    elif dir == 1:  # horizontal left
        x = x - 1
    elif dir == 2:  # vertical up
        y = y - 1
    elif dir == 3:  # vertical down
        y = y + 1
    elif dir == 4:  # diag ul
        y = y - 1
        x = x - 1
    elif dir == 5:  # diag dl
        y = y + 1
        x = x - 1
    elif dir == 6:  # diag ur
        y = y - 1
        x = x + 1
    elif dir == 7:  # diag dr
        y = y + 1
        x = x + 1

    if y < 0 or x < 0 or y >= len(input) or x >= len(input[y]):
        return False

    if currchar == "X" and input[y][x] == "M":
        return check(y, x, "M", dir)
    elif currchar == "M" and input[y][x] == "A":
        return check(y, x, "A", dir)
    elif currchar == "A" and input[y][x] == "S":
        return True

    return False


total = 0
for y, line in enumerate(input):
    for x, char in enumerate(line):
        if char != "X":
            continue

        for dir in range(0, 8):
            if check(y, x, char, dir):
                total += 1

print(total)
