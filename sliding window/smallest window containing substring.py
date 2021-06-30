# Given a string and a pattern, 
# find the smallest substring in the given string which has all the characters of the given pattern.

# Example:
# Input: String="aabdec", Pattern="abc"
# Output: "abdec"
# Explanation: The smallest substring having all characters of the pattern is "abdec"

# sliding window:O(N + M) (M is the number of characters in pattern string) 
# space:O(K)-> O(M)(M is the worst case) (k is the number of distinct letters in string pattern)

def smallest_window_containing_substring(str, pattern):
    window_start, matched, substr_start = 0, 0, 0
    min_length = len(str) + 1
    char_pattern = dict()

    for char in pattern:
        if char not in char_pattern:
            char_pattern[char] = 0
        char_pattern[char] += 1
    
    for window_end in range(len(str)):
        right_char = str[window_end]
        if right_char in char_pattern:
            char_pattern[right_char] -= 1
            if char_pattern[right_char] >= 0:
                matched += 1

        while matched == len(pattern):
            if min_length > window_end - window_start + 1:
                min_length = window_end - window_start + 1
                substr_start = window_start
            
            left_char = str[window_start]
            window_start += 1
            if left_char in char_pattern:
                if char_pattern[left_char] == 0:
                    matched -= 1
                char_pattern[left_char] += 1
        
    if min_length > len(str):
        return ""
    return str[substr_start:substr_start+min_length]

print(smallest_window_containing_substring("aabdec","abc"))
print(smallest_window_containing_substring("abdabca","abc"))
print(smallest_window_containing_substring("adcad","abc"))
