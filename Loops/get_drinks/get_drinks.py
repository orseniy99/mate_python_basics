def get_drinks(number_of_guests: int) -> int:
    # write your code here
    cups = 0
    for i in range(number_of_guests + 1):
      cups += i
    return cups