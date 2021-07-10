# Given a list of intervals representing the start and end time of ‘N’ meetings, 
# find the minimum number of rooms required to hold all the meetings.

# Example:
# Meetings: [[4,5], [2,3], [2,4], [3,5]]
# Output: 2
# Explanation: We will need one room for [2,3] and [3,5], and another room for [2,4] and [4,5].

# O(NlogN) (sort :O(NlogN) and push/pop O(logN) for each iteration, overall iterate for N times)
# space: O(N)

from heapq import *

class Meeting:
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end
    
    def __lt__(self, other):
        return self.end < other.end

def min_meeting_rooms(arr):
    meetings = []
    for i in arr:
        meetings.append(Meeting(i[0], i[1]))
    
    meetings.sort(key = lambda x: x.start)

    min_rooms = 0
    min_heap = []

    for meeting in meetings:
        while len(min_heap) > 0 and meeting.start >= min_heap[0].end:
            heappop(min_heap)
        
        heappush(min_heap, meeting)

        min_rooms = max(min_rooms, len(min_heap))
    
    return min_rooms

print(min_meeting_rooms([[1,4], [2,5], [7,9]]))
print(min_meeting_rooms([[6,7], [2,4], [8,12]]))
print(min_meeting_rooms([[1,4], [2,3], [3,6]]))
print(min_meeting_rooms([[4,5], [2,3], [2,4], [3,5]]))

# follow up :
# Problem 1: Given a list of intervals, find the point where the maximum number of intervals overlap.
# ??? don't know how to solve

# Problem 2: Given a list of intervals representing the arrival and departure times of trains to a train station, 
# our goal is to find the minimum number of platforms required for the train station so that no train has to wait.
# Problem 2 is equal to the minimum meeting room