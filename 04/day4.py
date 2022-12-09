def contains(r1, r2):
    if (r1[0] >= r2[0] and r1[1] <= r2[1]) or (r2[0] >= r1[0] and r2[1] <= r1[1]):
        return True
    else:
        return False
        
with open('input.txt') as input:
    tot = 0
    for line in input:
        line = line.strip()
        rs = line.split(',')
        if contains([int(x) for x in rs[0].split('-')], [int(x) for x in rs[1].split('-')]):
            tot += 1        
print(tot)