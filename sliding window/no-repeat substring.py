# Given a string, find the length of the longest substring which has no repeating characters.
# Example:
# Input: String="aabccbb"
# Output: 3
# Explanation: The longest substring without any repeating characters is "abc".

# sliding window: O(N) space: O(K) (k is the number of distinct characters in the string)-> O(1)
def no_repeat_substring(str):
    result = 0
    window_start = 0
    char_index_map = dict()
    for window_end in range(len(str)):
        right_char = str[window_end]
        if right_char in char_index_map:
            window_start = max(window_start, char_index_map[right_char] + 1)
        char_index_map[right_char] = window_end
        result = max(result, window_end-window_start+1)
    return result

print(no_repeat_substring("aabccbb"))