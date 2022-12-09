with open('input.txt') as input:
    tot = 0
    totmax = [0,0,0]
    for line in input:
        line = line.strip()
        if line:
            tot += int(line)
        else:
            if tot > totmax[0]:
                totmax[0] = tot
                totmax.sort()
            tot = 0
print(sum(totmax))