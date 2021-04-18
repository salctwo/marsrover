
"""
car: parameter correspond to the rover state, tuple data structure e.g. (0,0,N)
command: parameter correspond to only one letter command e.g. R or L or M 

Note: from http calls commands are sequences of these letters e.g. RMMMRM 
but here consider command parameters just one letter 
(more info see post() function in the controller.py)
"""


def action (car, command):
    # Implement me

    (x,y,direction) = car

    new_direction = get_direction(direction, command)

    if command == 'M' and new_direction == 'N':
        y = move_y(y, new_direction)
    elif command == 'M' and new_direction == 'S':
        y = move_y(y, new_direction)


    return (x,y,new_direction)


def get_direction(direction, command):

    if direction == 'N' and command == 'L':
        return 'W'

    elif direction == 'N' and command == 'R':
        return 'E'

    elif direction == 'S' and command == 'L':
        return 'W'

    elif direction == 'S' and command == 'R':
        return 'E'

    elif direction == 'E' and command == 'L':
        return 'N'

    elif direction == 'E' and command == 'R':
        return 'S'

    elif direction == 'W' and command == 'L':
        return 'S'

    #else:
        #return 'N'

    elif direction == 'W' and command == 'R':
        return 'N'

def move_x():
    pass

def move_y(y, direction):

    if direction == 'N':
        y = (y - 1) % 10
        return y
    else:
        y = (y + 1) % 10
        return y


# command solo recibe una letra:
    # R o L
    # M 
 
 # x = (x + numero) % 10
 # angle tambien puede ser con modulo, base 4
    # ex, N = 0
    # L = -1 