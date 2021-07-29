# Given a string, sort it based on the decreasing frequency of its characters.

# Example:
# Input: "Programming"
# Output: "rrggmmPiano"
# Explanation: 'r', 'g', and 'm' appeared twice, so they need to appear before any other character.

# O(N* logN) space: O(N)

from heapq import *

class WordFrequency:
    def __init__(self, word, frequency) -> None:
        self.word = word
        self.frequency = frequency
    
    def __lt__(self, other):
        return self.frequency < other.frequency
    

def frequency_sort(input_str):
    hashmap = dict()
    for word in input_str:
        hashmap[word] = hashmap.get(word, 0) + 1
        
    minheap = []
    for key, val in hashmap.items():
        heappush(minheap, WordFrequency(key, val))
    
    result = ''
    while minheap:
        word_frequency = heappop(minheap)
        for _ in range(word_frequency.frequency):
            result = word_frequency.word + result
    
    return result

print(frequency_sort("Programming"))
print(frequency_sort("abcbab"))