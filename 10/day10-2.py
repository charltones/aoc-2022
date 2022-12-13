with open('input.txt') as input:
    register = 1
    cycle = 1
    screen_width = 40
    interesting_cycle = screen_width
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
                if (cycle-1) % screen_width in [register-1, register, register+1]:
                    print('#', end='')
                else:
                    print('.', end='')
                if cycle==interesting_cycle:
                    interesting_cycle += 40
                    print('')
                cycle += 1
                cycles_left -= 1
            if line=='addx':
                register += int(value)
