# Permutation is defined as the re-arranging of the characters of the string
# Given a string and a pattern, find out if the string contains any permutation of the pattern.

# Example:
# Input: String="oidbcaf", Pattern="abc"
# Output: true
# Explanation: The string contains "bca" which is a permutation of the given pattern.

# Input: String="odicf", Pattern="dc"
# Output: false
# Explanation: No permutation of the pattern is present in the given string as a substring.

# sliding window:O(N + M) (M is the number of characters in pattern string) 
# space:O(K)-> O(M)(M is the worst case) (k is the number of distinct letters in string pattern)

def permutation_in_a_string(str, pattern):
    char_pattern = dict()
    for char in pattern:
        if char not in char_pattern:
            char_pattern[char] = 0
        char_pattern[char] += 1
    window_start = 0
    char_frequency = dict()
    for window_end in range(len(str)):
        right_char = str[window_end]
        if right_char not in char_frequency:
            char_frequency[right_char] = 0
        char_frequency[right_char] += 1
        if window_end - window_start + 1 > len(pattern):
            left_char = str[window_start]
            char_frequency[left_char] -= 1
            if char_frequency[left_char] == 0:
                del char_frequency[left_char]
            window_start += 1
        if char_frequency == char_pattern:
            return True
    return False

print(permutation_in_a_string("oidbcaf", "abc"))
print(permutation_in_a_string("odicf", "dc"))
print(permutation_in_a_string("bcdxabcdy", "bcdyabcdx"))
print(permutation_in_a_string("aaacb", "abc"))

def permutation_in_a_string_2(str, pattern):
    window_start, matched = 0, 0
    char_frequency = dict()
    for char in pattern:
        if char not in char_frequency:
            char_frequency[char] = 0
        char_frequency[char] += 1 
    
    for window_end in range(len(str)):
        right_char = str[window_end]
        if right_char in char_frequency:
            char_frequency[right_char] -= 1
            if char_frequency[right_char] == 0:
                matched += 1

        if matched == len(char_frequency):
            return True
        
        if window_end >= len(pattern) - 1:
            left_char = str[window_start]
            window_start += 1
            if left_char in char_frequency:
                if char_frequency[left_char] == 0:
                    matched -= 1
                char_frequency[left_char] += 1
    
    return False

print(permutation_in_a_string_2("oidbcaf", "abc"))
print(permutation_in_a_string_2("odicf", "dc"))
print(permutation_in_a_string_2("bcdxabcdy", "bcdyabcdx"))
print(permutation_in_a_string_2("aaacb", "abc"))