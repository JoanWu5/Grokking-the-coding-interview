# Every non-negative integer N has a binary representation, 
# for example, 8 can be represented as “1000” in binary and 7 as “0111” in binary.

# The complement of a binary representation is the number in binary that 
# we get when we change every 1 to a 0 and every 0 to a 1. For example, the binary complement of “1010” is “0101”.
# For a given positive number N in base-10, return the complement of its binary representation as a base-10 integer.

# Example:
# Input: 8
# Output: 7
# Explanation: 8 is 1000 in binary, its complement is 0111 in binary, which is 7 in base-10.

# time: O(logN) space: O(1)
def complement_base_ten_number(number):
    bit_count = 1
    while bit_count <= number:
        bit_count = bit_count << 1

    return number ^ (bit_count - 1)

print(complement_base_ten_number(8))
print(complement_base_ten_number(10))