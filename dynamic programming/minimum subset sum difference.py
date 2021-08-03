# Given a set of positive numbers, partition the set into two subsets with minimum difference between their subset sums.

# Example:
# Input: {1, 2, 3, 9}
# Output: 3
# Explanation: We can partition the given set into two subsets where minimum absolute difference 
# between the sum of numbers is '3'. Following are the two subsets: {1, 2, 3} & {9}.

# brute force
# O(2^N) space:O(N)
def minimum_subset_sum_difference_1(nums):
    return minimum_subset_sum_difference_1_recursive(nums, 0, 0, 0)

def minimum_subset_sum_difference_1_recursive(nums, current_index, sum1, sum2):
    if current_index >= len(nums):
        return abs(sum1 - sum2)
    
    diff1 = minimum_subset_sum_difference_1_recursive(nums, current_index + 1, sum1 + nums[current_index], sum2)
    diff2 = minimum_subset_sum_difference_1_recursive(nums, current_index + 1, sum1, sum2 + nums[current_index])
    return min(diff1, diff2)

print(minimum_subset_sum_difference_1([1, 2, 3, 9]))
print(minimum_subset_sum_difference_1([1, 2, 7, 1, 5]))
print(minimum_subset_sum_difference_1([1, 3, 100, 4]))

# top-down dp
def minimum_subset_sum_difference_2(nums):
    s = sum(nums)
    dp = [[-1 for _ in range(s + 1)] for _ in range(len(nums))]
    return minimum_subset_sum_difference_2_recursive(dp, nums, 0, 0, 0)

# O(N * S) where ‘N’ represents total numbers and ‘S’ is the total sum of all the numbers.
# space: O(N * S)
def minimum_subset_sum_difference_2_recursive(dp, nums, current_index, sum1, sum2):
    if current_index >= len(nums):
        return abs(sum1 - sum2)
    
    if dp[current_index][sum1] == -1:
        diff1 = minimum_subset_sum_difference_2_recursive(dp, nums, current_index + 1, sum1 + nums[current_index], sum2)
        diff2 = minimum_subset_sum_difference_2_recursive(dp, nums, current_index + 1, sum1, sum2 + nums[current_index])
        dp[current_index][sum1] = min(diff1, diff2)
    
    return dp[current_index][sum1]

print(minimum_subset_sum_difference_2([1, 2, 3, 9]))
print(minimum_subset_sum_difference_2([1, 2, 7, 1, 5]))
print(minimum_subset_sum_difference_2([1, 3, 100, 4]))

# bottom-up dp
# O(N * S) space: O(N * S)
def minimum_subset_sum_difference_3(nums):
    s = sum(nums)
    dp = [[False for _ in range(int(s/2) + 1)] for _ in range(len(nums))]
    for i in range(len(nums)):
        dp[i][0] = True
    
    for j in range(int(s/2) + 1):
        dp[0][j] = nums[0] == j
    
    for i in range(1, len(nums)):
        for j in range(1, int(s/2) + 1):
            if dp[i - 1][j]:
                dp[i][j] = dp[i - 1][j]
            elif j >= nums[i]:
                dp[i][j] = dp[i - 1][j - nums[i]]
    
    sum1 = 0
    for i in range(int(s/2), -1, -1):
        if dp[len(nums) - 1][i]:
            sum1 = i
            break
    
    sum2 = s - sum1
    return abs(sum1 - sum2)

print(minimum_subset_sum_difference_3([1, 2, 3, 9]))
print(minimum_subset_sum_difference_3([1, 2, 7, 1, 5]))
print(minimum_subset_sum_difference_3([1, 3, 100, 4]))