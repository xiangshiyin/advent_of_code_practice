import os

# cd into the current directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# 1. Read the input file
reports = []
# with open("20241202_input_example.txt", "r") as file:
with open("20241202_input.txt", "r") as file:
    for line in file:
        reports.append(list(map(int, line.split())))

# 2. Find the total number of reports that are safe
safe_reports = 0
# rules:
# 1. The difference between any two adjacent numbers is at most 3
# 2. The difference between any two adjacent numbers is at least 1
# 3. The sequence is either strictly increasing or strictly decreasing
# 4. If removing a single number from an unsafe report would make it safe, the report instead counts as safe.


def is_safe(report):
    return all(report[i] < report[i+1] and report[i+1] - report[i] <= 3 and report[i+1] - report[i] >= 1 for i in range(len(report) - 1)) or all(report[i] > report[i+1] and report[i] - report[i+1] <= 3 and report[i] - report[i+1] >= 1 for i in range(len(report) - 1))

for report in reports:
    if is_safe(report):
        safe_reports += 1
    else:
        for i in range(len(report)):
            if is_safe(report[:i] + report[i+1:]):
                safe_reports += 1
                break

print(safe_reports)
