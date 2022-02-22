def get_tips_rating(amount: int) -> str:
    # write your code here
    if amount == 0:
        return 'terrible'
    elif amount <= 10:
        return 'poor'
    elif amount >= 10 and amount <=20:
        return 'good'
    elif amount >= 20 and amount <=50:
        return 'great'
    else:
        return "excellent"
