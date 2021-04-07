from_dir = {'N': 0, 'E': 1, 'S': 2, 'W': 3}
to_dir = {0: 'N', 1: 'E', 2: 'S', 3: 'W'}



def step(x,y, car):
    (cx,cy,cd) = car
    return ( (cx+x) % 10, (cy+y) % 10, cd)

def move_n(car):
    return step(-1,0,car)
def move_s(car):
    return step(1,0,car)
def move_e(car):
    return step(0,1,car)
def move_w(car):
    return step(0,-1,car)



move = {'N': move_n, 'E': move_e, 'S': move_s, 'W': move_w}

def action(car, command):
    (cx,cy,cd) = car
    if(command == 'M'):
        return move[cd](car)
    elif(command == 'L'):
        nd = (from_dir[cd] - 1) % 4
        return (cx,cy, to_dir[nd])
    elif(command == 'R'):
        nd = (from_dir[cd] + 1) % 4
        return (cx,cy, to_dir[nd])
    else:
        return car



