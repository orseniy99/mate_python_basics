def double_power(current_powers: list) -> list:
    # write your code here
    dbld = []
    for i in range(len(current_powers)):
        dbld.append(current_powers[i] * 2)
    return dbld
