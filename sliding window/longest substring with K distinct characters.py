# Given a string, find the length of the longest substring in it with no more than K distinct characters.
# Example:
# Input: String="araaci", K=2
# Output: 4
# Explanation: The longest substring with no more than '2' distinct characters is "araa".

# Input: String="cbbebi", K=3
# Output: 5
# Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".

# sliding window: O(N) space: O(K)
def longest_substring_with_k_distinct_characters(str, k):
    window_start = 0
    result = 0
    char_frequency = dict()
    for window_end in range(len(str)):
        right_char = str[window_end]
        if right_char not in char_frequency:
            char_frequency[right_char] = 0
        char_frequency[right_char] += 1
        while(len(char_frequency)) > k:
            left_char = str[window_start]
            char_frequency[left_char] -= 1
            if char_frequency[left_char] == 0:
                del char_frequency[left_char]
            window_start += 1
        result = max(result, window_end - window_start + 1)
    return result

print(longest_substring_with_k_distinct_characters("araaci", 2))
print(longest_substring_with_k_distinct_characters("araaci", 1))
print(longest_substring_with_k_distinct_characters("cbbebi", 3))