north = '⍓'
south = '⍌'
east = '⍄'
west = '⍃'

def render_car(dir):
    if(dir == 'N'):
        return north
    elif(dir == 'S'):
        return south
    elif(dir == 'E'):
        return east
    elif(dir == 'W'):
        return west
    else:
        return north


def render_grid(car):
    result = ''
    (c_x, c_y, c_d) = car
    til = range(0,10)
    for y in til:
        row = str(y)
        for x in til:
            if(c_x == x and c_y == y):
                cell = render_car(c_d)
            else:
                cell = '_'
            row = row + ' ' + cell  
        if(y == 0):
            result = result + '  '+' '.join(map(str,list(til)))  
        result = result +'\n'+row
        row = ''
    return result
