# There is a dictionary containing words from an alien language for which we don’t know the ordering of the characters. 
# Write a method to find the correct order of characters in the alien language.

# Example:
# Input: Words: ["ba", "bc", "ac", "cab"]
# Output: bac
# Explanation: Given that the words are sorted lexicographically by the rules of the alien language, so
# from the given words we can conclude the following ordering among its characters:
# 1. From "ba" and "bc", we can conclude that 'a' comes before 'c'.
# 2. From "bc" and "ac", we can conclude that 'b' comes before 'a'
# From the above two points, we can conclude that the correct character order is: "bac"

# O(V + N) space: O(V + N)
from collections import deque

def alien_language(words):
    if words is None or len(words) == 0:
        return ""
    
    indegree = dict()
    graph = dict()

    for word in words:
        for char in word:
            indegree[char] = 0
            graph[char] = []
    
    for i in range(len(words) - 1):
        word1, word2 = words[i], words[i + 1]
        for j in range(min(len(word1), len(word2))):
            parent, child = word1[j], word2[j]
            if parent != child:
                graph[parent].append(child)
                indegree[child] += 1
                break

    sources = deque()
    for key, value in indegree.items():
        if value == 0:
            sources.append(key)

    order = []

    while sources:
        parent = sources.popleft()
        order.append(parent)
        children = graph[parent]
        for child in children:
            indegree[child] -= 1
            if indegree[child] == 0:
                sources.append(child)
    
    if len(order) != len(indegree):
        return ""
    
    return "".join(order)

print(alien_language(["ba", "bc", "ac", "cab"]))
print(alien_language(["cab", "aaa", "aab"]))
print(alien_language(["ywx", "wz", "xww", "xz", "zyy", "zwz"]))