# Given a string and a list of words, find all the starting indices of substrings in the given string 
# that are a concatenation of all the given words exactly once without any overlapping of words. 
# It is given that all words are of the same length.

# Example:
# Input: String="catfoxcat", Words=["cat", "fox"]
# Output: [0, 3]
# Explanation: The two substring containing both the words are "catfox" & "foxcat".

# sliding window: O(N*M*len) (where ‘N’ is the number of characters in the given string, 
# ‘M’ is the total number of words, and ‘Len’ is the length of a word.)
# space: O(M + N) (hashMap + result array)

def word_concatenation(str, words):
    if len(words) == 0 or len(words[0]) == 0:
        return []

    result = []
    word_pattern = dict()
    word_length = len(words[0])
    word_count = len(words)

    for word in words:
        if word not in word_pattern:
            word_pattern[word] = 0
        word_pattern[word] += 1
    
    for window_start in range(len(str)-word_count*word_length+1):
        word_seen = dict()
        for j in range(word_count):
            next_word_index = window_start + j * word_length
            word = str[next_word_index:next_word_index+word_length]
            if word not in word_pattern:
                break
            
            if word not in word_seen:
                word_seen[word] = 0
            word_seen[word] += 1

            if word_seen[word] > word_pattern[word]:
                break

            if j + 1 == word_count:
                result.append(window_start)
    
    return result

print(word_concatenation("catfoxcat", ["cat", "fox"]))
print(word_concatenation("catcatfoxfox", ["cat", "fox"]))