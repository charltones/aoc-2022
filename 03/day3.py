with open('input.txt') as input:
    tot = 0
    group = []
    for line in input:
        line = line.strip()
        half = len(line)//2
        common = list(set(line[:half]) & set(line[half:]))
        if common and len(common)==1:
            p = ord(common[0].swapcase())-64
            prio = p-6 if p>32 else p
            tot += prio
print(tot)