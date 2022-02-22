def scrolling_text(string: str) -> list:
    # write your code here
    shift = [string.upper()]
    for i in range(len(string)):
        shift_to_list = list(shift[-1])
        shift_to_list.append(shift_to_list.pop(0))
        list_to_string =''.join([str(char) for char in shift_to_list])
        shift.append(list_to_string)
    return shift[:-1]