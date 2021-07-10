# We are given a list of Jobs. Each job has a Start time, an End time, and a CPU load when it is running. Our goal is to find the maximum CPU load at any time if all the jobs are running on the same machine.

# Example:
# Jobs: [[1,4,3], [2,5,4], [7,9,6]]
# Output: 7
# Explanation: Since [1,4,3] and [2,5,4] overlap, their maximum CPU load (3+4=7) will be when both the 
# jobs are running at the same time i.e., during the time interval (2,4).

from heapq import heappop, heappush


class Job:
    def __init__(self, start, end, cpu_load) -> None:
        self.start = start
        self.end = end
        self.cpu_load = cpu_load

    def __lt__(self, other):
        return self.end < other.end

def max_cpu_load(arr):
    jobs = []
    for item in arr:
        jobs.append(Job(item[0], item[1], item[2]))
    
    max_cpu_load = 0
    current_cpu_load = 0
    min_heap = []
    jobs.sort(key = lambda x: x.start)

    for job in jobs:
        while len(min_heap) > 0 and job.start >= min_heap[0].end:
            current_cpu_load -= min_heap[0].cpu_load
            heappop(min_heap)

        heappush(min_heap, job)
        current_cpu_load += job.cpu_load
        max_cpu_load = max(max_cpu_load, current_cpu_load)

    return max_cpu_load

print(max_cpu_load([[1,4,3], [2,5,4], [7,9,6]]))
print(max_cpu_load([[6,7,10], [2,4,11], [8,12,15]]))
print(max_cpu_load([[1,4,2], [2,4,1], [3,6,5]]))

print(max_cpu_load([[1,4,3], [4,5,2], [2,3,0]]))
    
