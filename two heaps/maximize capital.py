# Given a set of investment projects with their respective profits, 
# we need to find the most profitable projects. 
# We are given an initial capital and are allowed to invest only in a fixed number of projects. 
# Our goal is to choose projects that give us the maximum profit.
# We can start an investment project only when we have the required capital. 
# Once a project is selected, we can assume that its profit has become our capital.

# Example:
# Input: Project Capitals=[0,1,2], Project Profits=[1,2,3], Initial Capital=1, Number of Projects=2
# Output: 6
# Explanation:
# With initial capital of ‘1’, we will start the second project which will give us profit of ‘2’. 
# Once we selected our first project, our total capital will become 3 (profit + initial capital).
# With ‘3’ capital, we will select the third project, which will give us ‘3’ profit.
# After the completion of the two projects, our total capital will be 6 (1+2+3).

# O(NlogN + KlogN) where ‘N’ is the total number of projects and ‘K’ is the number of projects we are selecting.
# space: O(N)
from heapq import *

def find_maximize_capital(capitals, profits, initial_capital, num_projects):
    max_heap = []
    min_heap = []

    for i in range(len(capitals)):
        heappush(min_heap, (capitals[i], i))
    
    available_capital = initial_capital
    for _ in range(num_projects):
        while min_heap and min_heap[0][0] <= available_capital:
            _, i = heappop(min_heap)
            heappush(max_heap, (-profits[i], i))
    
        if not max_heap:
            break

        available_capital += -heappop(max_heap)[0]
    
    return available_capital

print(find_maximize_capital([0, 1, 2], [1, 2, 3], 1, 2))
print(find_maximize_capital([0, 1, 2, 3], [1, 2, 3, 5], 0, 3))