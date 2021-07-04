# Given an array of unsorted numbers and a target number, 
# find all unique quadruplets in it, whose sum is equal to the target number.

# Example:
# Input: [4, 1, 2, -1, 1, -3], target=1
# Output: [-3, -1, 1, 4], [-3, 1, 1, 2]
# Explanation: Both the quadruplets add up to the target.

def quadruple_sum_to_target(arr, target_sum):
    arr.sort()
    quadrupts = []
    for i in range(len(arr)-3):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        for j in range(i+1, len(arr)-2):
            if j > i+1 and arr[j] == arr[j-1]:
                continue
            search_pairs(arr, target_sum, i, j, quadrupts)
    return quadrupts

def search_pairs(arr, target_sum, first, second, quadrupts):
    left, right = second + 1, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right] + arr[first] + arr[second]
        if current_sum == target_sum:
            quadrupts.append([arr[first], arr[second], arr[left], arr[right]])
            left += 1
            right -= 1
            while left < right and arr[left] == arr[left - 1]:
                left += 1
            while left < right and arr[right] == arr[right + 1]:
                right -= 1
        elif current_sum > target_sum:
            right -= 1
        else:
            left += 1

print(quadruple_sum_to_target([4, 1, 2, -1, 1, 1, -3], 1))
print(quadruple_sum_to_target([2, 0, -1, 1, -2, 2], 2))