# Given a list of intervals, 
# merge all the overlapping intervals to produce a list that has only mutually exclusive intervals.

# Example:
# Intervals: [[1,4], [2,5], [7,9]]
# Output: [[1,5], [7,9]]
# Explanation: Since the first two intervals [1,4] and [2,5] overlap, we merged them into one [1,5].


# O(N) for merge O(NlogN) for sorting -> O(NlogN)
# space:O(N)
class Interval:
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end
    
    def print_interval(self):
        print("[" + str(self.start) + "," + str(self.end) + "]", end='')


def merge_intervals(arr):
    intervals = []
    for i in arr:
        intervals.append(Interval(i[0], i[1]))

    if len(intervals) < 2:
        return intervals

    intervals.sort(key = lambda x: x.start)

    merged_intervals = []
    start = intervals[0].start
    end = intervals[0].end

    for i in range(1, len(intervals)):
        interval = intervals[i]
        if interval.start <= end:
            end = max(interval.end, end)
        else:
            merged_intervals.append(Interval(start, end))
            start = interval.start
            end = interval.end

    merged_intervals.append(Interval(start, end))
    return merged_intervals

for i in merge_intervals([[1,4], [2,5], [7,9]]):
    i.print_interval()
print()

for i in merge_intervals([[6,7], [2,4], [5,9]]):
    i.print_interval()
print()

for i in merge_intervals([[1,4], [2,6], [3,5]]):
    i.print_interval()
print()