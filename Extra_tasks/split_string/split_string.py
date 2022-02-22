def split_string(string: str) -> list:
    # write your code here
    import re
    if len(string) % 2 == 0:
        splitted = re.findall('..?', string)
        return splitted
    else:
        splitted = re.findall('..?', string)
        splitted [-1] += '_'
        return splitted

