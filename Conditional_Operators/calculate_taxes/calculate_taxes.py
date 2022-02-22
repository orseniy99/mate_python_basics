def calculate_taxes(income: int) -> float:
    # write your code here
    if income <= 1000:
        perc = 0.02
    elif 1000 < income <= 10000:
        perc = 0.03
    else:
        perc = 0.05

    return income * perc
