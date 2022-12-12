def move_one(hp, tp, dirn):
    if dirn=='L':
        hp = (hp[0] - 1, hp[1])
    elif dirn=='R':
        hp = (hp[0] + 1, hp[1])
    elif dirn=='U':
        hp = (hp[0], hp[1] - 1)
    elif dirn=='D':
        hp = (hp[0], hp[1] + 1)
    xd = hp[0] - tp[0]
    yd = hp[1] - tp[1]
    if abs(xd)==2:
        tp = (tp[0] + xd // 2, tp[1] + yd)
    elif abs(yd)==2:
        tp = (tp[0] + xd, tp[1] + yd // 2)
    return (hp, tp)

with open('input.txt') as input:
    headpos = (0,0)
    tailpos = (0,0)
    visits = set()
    for line in input:
        line = line.strip()
        if line:
            (dirn, dist) = line.split()
            for m in range(int(dist)):
                (headpos, tailpos) = move_one(headpos, tailpos, dirn)
                visits.add(tailpos)
print(len(visits))