# Given a string, find if its letters can be rearranged in such a way that no two same characters come next to each other.

# Example:
# Input: "aappp"
# Output: "papap"
# Explanation: In "papap", none of the repeating characters come next to each other.

# O(N * logN) space: O(N)
from heapq import *

def rearrange_string(input_str):
    maxheap = []
    hashmap = dict()
    for char in input_str:
        hashmap[char] = hashmap.get(char, 0) + 1
    
    for char, frequency in hashmap.items():
        heappush(maxheap, (-frequency, char))
    
    result = []
    previous_char, previous_frequency = None, 0
    while maxheap:
        frequency, char = heappop(maxheap)
        if previous_char and -previous_frequency > 0:
            heappush(maxheap, (previous_frequency, previous_char))
        result.append(char)
        previous_char = char
        previous_frequency = frequency + 1
    
    if len(result) == len(input_str):
        return "".join(result)
    else:
        return ""


print(rearrange_string("aappp"))
print(rearrange_string("Programming"))
print(rearrange_string("aapa"))