def get_largest_expression_result(a, b):
    # write your code here
    add = a + b
    sub = a - b
    mul = a * b
    div = a / b
    a = [add, sub, mul, div]
    return max(a)