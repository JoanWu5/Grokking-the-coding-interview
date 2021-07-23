# Given an expression containing digits and operations (+, -, *), 
# find all possible ways in which the expression can be evaluated by grouping the numbers and operators using parentheses.

# Example:
# Input: "1+2*3"
# Output: 7, 9
# Explanation: 1+(2*3) => 7 and (1+2)*3 => 9

def evaluate_expression_result(input_str):
    return  evaluate_expression({}, input_str)

# O(N * 2^N) space: O(N * 2^N)
def evaluate_expression(map, input_str):
    if input_str in map:
        return map[input_str]

    result = []
    if '+' not in input_str and '-' not in input_str and '*' not in input_str:
        result.append(int(input_str))
    else:
        for i in range(len(input_str)):
            char = input_str[i]
            if not char.isdigit():
                left_part = evaluate_expression(map, input_str[0:i])
                right_part = evaluate_expression(map, input_str[i+1:])
                for part1 in left_part:
                    for part2 in right_part:
                        if char == '+':
                            result.append(part1 + part2)
                        elif char == '-':
                            result.append(part1 - part2)
                        elif char == '*':
                            result.append(part1 * part2)
    
    map[input_str] = result
    return result

print(evaluate_expression_result("1+2*3"))
print(evaluate_expression_result("2*3-4-5"))