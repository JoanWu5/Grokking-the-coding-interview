# Given a string and a pattern, find all anagrams of the pattern in the given string.
# Anagram is actually a Permutation of a string.

# Example:
# Input: String="ppqp", Pattern="pq"
# Output: [1, 2]
# Explanation: The two anagrams of the pattern in the given string are "pq" and "qp".

# Input: String="abbcabc", Pattern="abc"
# Output: [2, 3, 4]
# Explanation: The three anagrams of the pattern in the given string are "bca", "cab", and "abc".

# sliding window:O(N + M) (M is the number of characters in pattern string) 
# space:O(K)-> O(M)(M is the worst case) (k is the number of distinct letters in string pattern)

def string_anagram(str, pattern):
    window_start, matched = 0, 0
    result = []
    char_pattern = dict()
    
    for char in pattern:
        if char not in char_pattern:
            char_pattern[char] = 0
        char_pattern[char] += 1
    
    for window_end in range(len(str)):
        right_char = str[window_end]
        if right_char in char_pattern:
            char_pattern[right_char] -= 1
            if char_pattern[right_char] == 0:
                matched += 1
        
        if matched == len(char_pattern):
            result.append(window_start)
        
        if window_end >= len(pattern) -1:
            left_char = str[window_start]
            window_start += 1
            if left_char in char_pattern:
                if char_pattern[left_char] == 0:
                    matched -= 1
                char_pattern[left_char] += 1
    return result

print(string_anagram("ppqp","pq"))
print(string_anagram("abbcabc","abc"))