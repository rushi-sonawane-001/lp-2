# Job Scheduling Algorithm

jobs = [
    ['A', 2, 100],
    ['B', 1, 19],
    ['C', 2, 27],
    ['D', 1, 25],
    ['E', 3, 15]
]

# Sort jobs by profit (highest first)
jobs.sort(key=lambda x: x[2], reverse=True)

slots = [False] * 3
result = []

total_profit = 0

for job in jobs:

    job_id = job[0]
    deadline = job[1]
    profit = job[2]

    # Check slots from deadline to 0
    for i in range(deadline - 1, -1, -1):

        if slots[i] == False:

            slots[i] = True
            result.append(job_id)

            total_profit += profit
            break

print("Scheduled Jobs:", result)

print("Total Profit:", total_profit)