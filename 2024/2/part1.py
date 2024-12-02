reports: list[str] = []

with open("input") as f:
    for line in f.readlines():
        reports.append(list(map(int, line.split())))


def check_safe(val1, val2):
    return abs(val1 - val2) <= 3


def check_graduality(report):
    if report[0] > report[1]:
        method = lambda l1, l2: l1 > l2
    else:
        method = lambda l1, l2: l1 < l2

    for i in range(len(report) - 1):
        if not method(report[i], report[i + 1]):
            return False
    return True


safe = 0
for report in reports:
    issafe = check_graduality(report)
    print(issafe)
    for i in range(len(report) - 1):
        issafe = issafe and check_safe(report[i], report[i + 1])

    if issafe:
        safe += 1

print(f"Safe: {safe}")
