# You are given a list of tasks that need to be run, in any order, on a server. 
# Each task will take one CPU interval to execute but once a task has finished, 
# it has a cooling period during which it can’t be run again. 
# If the cooling period for all tasks is ‘K’ intervals, 
# find the minimum number of CPU intervals that the server needs to finish all tasks.
# If at any time the server can’t execute any task then it must stay idle.

# Example:
# Input: [a, a, a, b, c, c], K=2
# Output: 7
# Explanation: a -> c -> b -> a -> c -> idle -> a

# O(N * logN) space: O(N)
from heapq import *


def schedule_tasks(tasks, k):
    hashmap = dict()
    for task in tasks:
        hashmap[task] = hashmap.get(task, 0) + 1
    
    maxheap = []
    for task, frequency in hashmap.items():
        heappush(maxheap, (-frequency, task))
    
    result = 0

    while maxheap:
        waitlist = []
        n = k + 1
        while n > 0 and maxheap:
            frequency, task = heappop(maxheap)
            result += 1
            if -frequency > 1:
                waitlist.append((frequency + 1, task))
            n -= 1
        
        for frequency, task in waitlist:
            heappush(maxheap, (frequency, task))
        
        if maxheap:
            result += n

    return result


print(schedule_tasks(['a', 'a', 'a', 'b', 'c', 'c'], 2))
print(schedule_tasks(['a', 'b', 'a'], 3))
