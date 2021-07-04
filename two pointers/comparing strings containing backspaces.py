# Given two strings containing backspaces (identified by the character ‘#’), 
# check if the two strings are equal.

# Example:
# Input: str1="xy#z", str2="xzz#"
# Output: true
# Explanation: After applying backspaces the strings become "xz" and "xz" respectively.

# O(M+N) where ‘M’ and ‘N’ are the lengths of the two input strings respectively. 
# space:O(1)
def comparing_string_contain_backspaces(str1, str2):
    pointer1, pointer2 = len(str1) - 1, len(str2) - 1
    while pointer1 >= 0 and pointer2 >= 0:
        i1 = get_next_valid_index(str1, pointer1)
        i2 = get_next_valid_index(str2, pointer2)
        if i1 < 0 and i2 < 0:
            return True

        if i1< 0 or i2 < 0:
            return False
        
        if str1[i1] != str2[i2]:
            return False

        pointer1 = i1 - 1
        pointer2 = i2 - 1

    return True

def get_next_valid_index(str, index):
    backspace_count = 0
    while index >= 0:
        if str[index] == '#':
            backspace_count += 1
        elif backspace_count > 0:
            backspace_count -= 1
        else:
            break

        index -= 1
    return index

print(comparing_string_contain_backspaces("xy#z", "xzz#"))
print(comparing_string_contain_backspaces("xy#z", "xyz#"))
print(comparing_string_contain_backspaces("xp#", "xyz##"))
print(comparing_string_contain_backspaces("xywrrmp", "xywrrmu#p"))