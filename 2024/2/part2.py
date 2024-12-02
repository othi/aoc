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


def remove_one(report: list[int]):
    reports = []
    for i in range(len(report)):
        reports.append(report[:i] + report[i + 1 :])
    return reports


safe = 0
for full_report in reports:
    full_report_issafe = False

    for report in remove_one(full_report):
        issafe = check_graduality(report)
        for i in range(len(report) - 1):
            issafe = issafe and check_safe(report[i], report[i + 1])

        if issafe:
            full_report_issafe = True
            break

    if full_report_issafe:
        safe += 1

print(f"Safe: {safe}")
