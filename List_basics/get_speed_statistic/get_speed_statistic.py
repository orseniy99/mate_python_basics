from math import floor


def get_speed_statistic(test_results: list) -> list:
    # write your code here
    if test_results:
        minimum = min(test_results)
        maximum = max(test_results)
        average = floor(sum(test_results) / len(test_results))
        return [minimum, maximum, average]
    else:
        return [0, 0, 0]
