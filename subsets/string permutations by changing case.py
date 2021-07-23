# Given a string, find all of its permutations preserving the character sequence but changing case.

# Example:
# Input: "ad52"
# Output: "ad52", "Ad52", "aD52", "AD52"

# O(N * 2^N) space: O(N * 2^N)
def string_permutation(str):
    permutations = []
    permutations.append(str)
    for i in range(len(str)):
        if str[i].isalpha():
            n = len(permutations)
            for j in range(n):
                character = list(permutations[j])
                character[i] = character[i].swapcase()
                permutations.append(''.join(character))
    
    return permutations

print(string_permutation("ad52"))

def find_letter_case_string_permutations(str):
    result = []
    generate_permutations_recursive(str, 0, [], result)
    return result

def generate_permutations_recursive(str, index, current_permutation, result):
    if index == len(str):
        result.append(''.join(current_permutation))
    else:
        if str[index].isalpha():
            for i in range(2):
                new_permutation = list(current_permutation)
                if i == 0:
                    new_permutation.append(str[index].lower())
                else:
                    new_permutation.append(str[index].upper())
                generate_permutations_recursive(str, index + 1, new_permutation, result)
        else:
            new_permutation = list(current_permutation)
            new_permutation.append(str[index])
            generate_permutations_recursive(str, index + 1, new_permutation, result)

print(find_letter_case_string_permutations("ad52"))
