def get_success_rate(statistics: str) -> int:
    # write your code here
    all = len(statistics)
    positive = 0
    for p in statistics:
        if p == '1':
            positive += 1
        else:
            pass

    return round((positive / all) * 100)