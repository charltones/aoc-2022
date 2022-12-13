with open('input.txt') as input:
    strengths = 0
    register = 1
    cycle = 1
    interesting_cycle = 20
    for line in input:
        line = line.strip()
        if line:
            if line=='noop':
                cycles_left = 1
            else:
                (line, value) = line.split()
                if line=='addx':
                    cycles_left = 2
                else:
                    print("ERROR", 4/0)
            while cycles_left > 0:
                #print("Cycle %d command %s arg %s register %d" % (cycle, line, (value or 'None'), register))
                if cycle==interesting_cycle:
                    signal_strength = cycle * register
                    strengths += signal_strength
                    print("**** Cycle %d register %d signal strength %d" % (cycle, register, signal_strength))
                    interesting_cycle += 40
                cycle += 1
                cycles_left -= 1
            if line=='addx':
                register += int(value)
                #print("Post Cycle %d command %s arg %s register %d" % (cycle-1, line, (value or 'None'), register))
print(strengths)