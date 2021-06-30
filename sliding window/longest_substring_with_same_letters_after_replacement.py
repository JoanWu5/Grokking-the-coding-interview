# Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters with any letter, 
# find the length of the longest substring having the same letters after replacement.

# Input: String="abbcb", k=1
# Output: 4
# Explanation: Replace the 'c' with 'b' to have a longest repeating substring "bbbb".

# sliding window:O(N) space:O(1)

def longest_substring_with_same_letters_after_k_replacement(str, k):
    char_frequency = dict()
    window_start = 0
    max_repeat_letter_count = 0
    result = 0
    for window_end in range(len(str)):
        right_char = str[window_end]
        if right_char not in char_frequency:
            char_frequency[right_char] = 0
        char_frequency[right_char] += 1
        max_repeat_letter_count = max(max_repeat_letter_count, char_frequency[right_char])
        if window_end - window_start + 1 - max_repeat_letter_count > k:
            left_char = str[window_start]
            char_frequency[left_char] -= 1
            window_start += 1
        result = max(result, window_end - window_start + 1)
    return result

print(longest_substring_with_same_letters_after_k_replacement("abbcb", 1))