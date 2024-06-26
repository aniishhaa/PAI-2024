def job_scheduling_greedy(jobs):
    jobs.sort(key=lambda x: x[1])  
    schedule = []
    last_finish_time = 0

    for job in jobs:
        start_time, finish_time, profit = job
        if start_time >= last_finish_time:
            schedule.append(job)
            last_finish_time = finish_time

    total_profit = sum(job[2] for job in schedule)
    return schedule, total_profit

jobs = [(1, 4, 20), (2, 5, 50), (6, 7, 70), (3, 8, 30)]
schedule, max_profit = job_scheduling_greedy(jobs)
print(f"Optimal schedule (greedy approach): {schedule}")
print(f"Maximum profit: {max_profit}")
