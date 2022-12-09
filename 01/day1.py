with open('input.txt') as input:
    tot = 0
    totmax = 0
    for line in input:
        line = line.strip()
        if line:
            tot += int(line)
        else:
            totmax = max(tot, totmax)
            tot = 0
print(totmax)