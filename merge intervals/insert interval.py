# Given a list of non-overlapping intervals sorted by their start time, 
# insert a given interval at the correct position and 
# merge all necessary intervals to produce a list that has only mutually exclusive intervals.

# Example:
# Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,6]
# Output: [[1,3], [4,7], [8,12]]
# Explanation: After insertion, since [4,6] overlaps with [5,7], we merged them into one [4,7].

# O(N)
# space: O(N)

def insert_interval(intervals, new_interval):
    merged_intervals = []
    i, start, end = 0, 0, 1

    while i < len(intervals) and intervals[i][end] < new_interval[start]:
        merged_intervals.append(intervals[i])
        i += 1
    
    while i < len(intervals) and intervals[i][start] <= new_interval[end]:
        new_interval[start] = min(intervals[i][start], new_interval[start])
        new_interval[end] = max(intervals[i][end], new_interval[end])
        i += 1
    
    merged_intervals.append(new_interval)

    while i < len(intervals):
        merged_intervals.append(intervals[i])
        i += 1
    
    return merged_intervals

print(insert_interval([[1,3], [5,7], [8,12]], [4,6]))
print(insert_interval([[1,3], [5,7], [8,12]], [4,10]))
print(insert_interval([[2,3],[5,7]], [1,4]))