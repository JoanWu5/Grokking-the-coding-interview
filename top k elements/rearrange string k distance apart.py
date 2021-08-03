# Given a string and a number ‘K’, 
# find if the string can be rearranged such that the same characters are at least ‘K’ distance apart from each other.

# Example:
# Input: "mmpp", K=2
# Output: "mpmp" or "pmpm"
# Explanation: All same characters are 2 distance apart.

# O(N * logN) space: O(N)
from heapq import *

def rearrange_string_k_distance_apart(input_str, k):
    maxheap = []
    hashmap = dict()
    for char in input_str:
        hashmap[char] = hashmap.get(char, 0) + 1
    
    for char, frequency in hashmap.items():
        heappush(maxheap, (-frequency, char))
    
    result = []
    previous_char, previous_frequency = [], []
    count = 1
    while maxheap:
        frequency, char = heappop(maxheap)
        if count >= k and previous_char[count - k] and -previous_frequency[count - k] > 0:
            heappush(maxheap, (previous_frequency[count - k], previous_char[count - k]))
        result.append(char)
        previous_char.append(char)
        previous_frequency.append(frequency + 1)
        count += 1
    
    if len(result) == len(input_str):
        return "".join(result)
    else:
        return ""

print(rearrange_string_k_distance_apart("mmpp", 2))
print(rearrange_string_k_distance_apart("Programming", 3))
print(rearrange_string_k_distance_apart("aab", 2))
print(rearrange_string_k_distance_apart("aappa", 3))


# to refine the solution, we can replace result = [] with deque()
# O(N * logN) space: O(N)

from collections import deque

def rearrange_string_k_distance_apart_2(input_str, k):
    maxheap = []
    hashmap = dict()
    for char in input_str:
        hashmap[char] = hashmap.get(char, 0) + 1
    
    for char, frequency in hashmap.items():
        heappush(maxheap, (-frequency, char))
    
    result = []
    queue = deque()

    while maxheap:
        frequency, char = heappop(maxheap)
        result.append(char)
        queue.append((frequency + 1, char))
        if len(queue) == k:
            frequency, char = queue.popleft()
            if -frequency > 0:
                heappush(maxheap, (-frequency, char))
    
    if len(result) == len(input_str):
        return "".join(result)
    else:
        return ""


print(rearrange_string_k_distance_apart_2("mmpp", 2))
print(rearrange_string_k_distance_apart_2("Programming", 3))
print(rearrange_string_k_distance_apart_2("aab", 2))
print(rearrange_string_k_distance_apart_2("aappa", 3))