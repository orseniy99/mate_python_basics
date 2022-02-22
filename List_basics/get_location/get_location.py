def get_location(coordinates: list, commands: list) -> list:
    # write your code here
    current_position = coordinates

    for command in commands:
        if command == 'forward':
            current_position[1] += 1
        elif command == 'back':
            current_position[1] -= 1
        elif command == 'right':
            current_position[0] += 1
        elif command == 'left':
            current_position[0] -= 1
        else:
            print('uknown command')
    return current_position
