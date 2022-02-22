def make_stickers(details_count: int, robot_part: str) -> list:
    # write you code here
    stickers = []
    if details_count != 0:
        for i in range(details_count):
            stickers.append(f'{robot_part} detail #{i+1}')
        return stickers
    else:
        return stickers
    