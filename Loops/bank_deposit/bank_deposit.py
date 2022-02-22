def calculate_profit(amount: int, percent: float, period: int) -> float:
    # write your code here
    balance = amount
    for i in range(period):
        balance += balance * (percent * 0.01)
    return(round(balance - amount, 2))
