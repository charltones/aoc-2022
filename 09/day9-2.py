def move_one(hp, dirn):
    if dirn=='L':
        hp = (hp[0] - 1, hp[1])
    elif dirn=='R':
        hp = (hp[0] + 1, hp[1])
    elif dirn=='U':
        hp = (hp[0], hp[1] - 1)
    elif dirn=='D':
        hp = (hp[0], hp[1] + 1)
    return hp
    
def catch_up(hp, tp):
    xd = hp[0] - tp[0]
    yd = hp[1] - tp[1]
    if abs(xd)==2 and abs(yd)==2:
        tp = (tp[0] + xd // 2, tp[1] + yd // 2)
    elif abs(xd)==2:
        tp = (tp[0] + xd // 2, tp[1] + yd)
    elif abs(yd)==2:
        tp = (tp[0] + xd, tp[1] + yd // 2)
    return tp

with open('input.txt') as input:
    snakepos = [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
    visits = set()
    for line in input:
        line = line.strip()
        if line:
            (dirn, dist) = line.split()
            for m in range(int(dist)):
                snakepos[0] = move_one(snakepos[0], dirn)
                for p in range(len(snakepos)-1):
                    snakepos[p+1] = catch_up(snakepos[p], snakepos[p+1])
                visits.add(snakepos[-1])
print(len(visits))