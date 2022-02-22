import math


def get_plan(current_production: int, month: int, percent: int):
    # write your code here
    plan = []
    prod = current_production
    for i in range(month):
        prod = int(math.floor(prod)) + int(math.floor(prod)) * (percent * 0.01)
        plan.append(int(math.floor(prod)))
    return plan
