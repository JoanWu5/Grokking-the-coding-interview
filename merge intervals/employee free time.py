# For ‘K’ employees, we are given a list of intervals representing the working hours of each employee. 
# Our goal is to find out if there is a free interval that is common to all employees. 
# You can assume that each list of employee working hours is sorted on the start time.

# Example:
# Input: Employee Working Hours=[[[1,3], [5,6]], [[2,3], [6,8]]]
# Output: [3,5]
# Explanation: Both the employess are free between [3,5].

# O(NlogK) (N is the number of intervals, k is the number of employees)
# space: O(K)
from heapq import *

class Interval:
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + "," + str(self.end) + "]", end= '')


class EmployeeInterval:
    def __init__(self, interval, employee_index, interval_index) -> None:
        self.interval = interval
        self.employee_index = employee_index
        self.interval_index = interval_index
    
    def __lt__(self, other):
        return self.interval.start < other.interval.start


def employee_free_time(arr):
    min_heap = []
    result = []
    employee_number = len(arr)
    for i in range(employee_number):
        heappush(min_heap, EmployeeInterval(Interval(arr[i][0][0], arr[i][0][1]), i, 0))

    previous_interval = min_heap[0].interval

    while min_heap:
        queue_top = heappop(min_heap)
        if previous_interval.end < queue_top.interval.start:
            result.append(Interval(previous_interval.end, queue_top.interval.start))
            previous_interval = queue_top.interval
        else:
            if previous_interval.end < queue_top.interval.end:
                previous_interval = queue_top.interval
        
        employee_schedule = arr[queue_top.employee_index]
        if len(employee_schedule) > queue_top.interval_index + 1:
            heappush(min_heap, EmployeeInterval(Interval(employee_schedule[queue_top.interval_index + 1][0], 
            employee_schedule[queue_top.interval_index + 1][1]), queue_top.employee_index, queue_top.interval_index + 1))
    
    return result

result = employee_free_time([[[1,3], [5,6]], [[2,3], [6,8]]])
for item in result:
    item.print_interval()
print()

result = employee_free_time([[[1,3], [9,12]], [[2,4]], [[6,8]]])
for item in result:
    item.print_interval()
print()

result = employee_free_time([[[1,3]], [[2,4]], [[3,5], [7,9]]])
for item in result:
    item.print_interval()
print()