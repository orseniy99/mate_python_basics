def is_werewolf(target: str) -> bool:
    # write your code here
    import re
    reverse = target[len(target)::-1]
    if re.sub('[^0-9a-zA-Z]+', '', target.lower()) == re.sub('[^0-9a-zA-Z]+', '', reverse.lower()):
        return True
    else:
        return False
