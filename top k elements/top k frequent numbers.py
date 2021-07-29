# Given an unsorted array of numbers, find the top ‘K’ frequently occurring numbers in it.

# Example:
# Input: [1, 3, 5, 12, 11, 12, 11], K = 2
# Output: [12, 11]
# Explanation: Both '11' and '12' apeared twice.

# O(N + N * logK) space: O(N)
from heapq import *

class WordFrequency:
    def __init__(self, word, frequency) -> None:
        self.word = word
        self.frequency = frequency
    
    def __lt__(self, other):
        return self.frequency < other.frequency


def top_k_frequent_elements(nums, k):
    hashmap = dict()
    for num in nums:
        if num not in hashmap:
            hashmap[num] = 1
        else:
            hashmap[num] += 1
    
    minheap = []
    for key, val in hashmap.items():
        heappush(minheap, WordFrequency(key, val))
        if len(minheap) > k:
            heappop(minheap)
    
    result = []
    while minheap:
        result.append(heappop(minheap).word)

    return result

print(top_k_frequent_elements([1, 3, 5, 12, 11, 12, 11], 2))
print(top_k_frequent_elements([5, 12, 11, 3, 11], 2))
