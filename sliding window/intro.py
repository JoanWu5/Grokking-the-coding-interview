# Given an array, find the average of all contiguous subarrays of size ‘K’ in it.
# Example: 
# Array: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5
# Output: [2.2, 2.8, 2.4, 3.6, 2.8]

# brute force
# time complexity : O(NK)

def find_average_of_subarrays(subarray, size):
    output = []
    for i in range(len(subarray)-size+1):
        average = sum(subarray[i: i+size])/size
        output.append(average)
    return output

subarray = [1, 3, 2, 6, -1, 4, 1, 8, 2]
size = 5
print(find_average_of_subarrays(subarray, size))
subarray = [1, 3, 2, 6, -1]
print(find_average_of_subarrays(subarray, size))
subarray = [1, 3, 2, 6]
print(find_average_of_subarrays(subarray, size))

# sliding window
# time complexity: O(N)

def find_average_of_subarrays_2(subarray, size):
    output = []
    result = sum(subarray[0:size])
    output.append(result/size)
    for i in range(len(subarray)-size):
        result -= subarray[i]
        result += subarray[i+size]
        output.append(result/size)
    return output

subarray = [1, 3, 2, 6, -1, 4, 1, 8, 2]
size = 5
print(find_average_of_subarrays_2(subarray, size))
subarray = [1, 3, 2, 6, -1]
print(find_average_of_subarrays_2(subarray, size))  

# mark answer
def find_average_of_subarrays_3(subarray, size):
    output = []
    windowSum, windowStart = 0, 0
    for windowEnd in range(len(subarray)):
        windowSum += subarray[windowEnd]
        if windowEnd >= size-1: # greater or equal to 
            output.append(windowSum/size)
            windowSum -= subarray[windowStart]
            windowStart += 1
    return output

subarray = [1, 3, 2, 6, -1, 4, 1, 8, 2]
size = 5
print(find_average_of_subarrays_3(subarray, size))
subarray = [1, 3, 2, 6, -1]
print(find_average_of_subarrays_3(subarray, size)) 