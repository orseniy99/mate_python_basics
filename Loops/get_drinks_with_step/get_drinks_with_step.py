def get_drinks_with_step(number_of_guests: int, step: int) -> int:
    # write your code here
    cups = 0
    for i in range(1, number_of_guests + 1, step):
      cups += i
    return cups
