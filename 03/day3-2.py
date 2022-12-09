with open('input.txt') as input:
    tot = 0
    group = []
    for line in input:
        line = line.strip()
        group.append(line)
        if len(group)==3:
            badge = list(set(group[0]) & set(group[1]) & set(group[2]))[0]
            if badge:
                p = ord(badge.swapcase())-64
                prio = p-6 if p>32 else p
                tot += prio
            group = []
print(tot)