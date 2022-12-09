import re
with open('input.txt') as input:
    stackrepr = []
    stacks = []
    moves = []
    for line in input:
        line = line.rstrip('\r\n')
        if line:
            matches = re.findall('....', line + '  ')
            stackrepr.append([re.findall('\w+',x) for x in matches])
        else:
            break
    stack_count = int(stackrepr.pop()[-1][0])
    stackrepr.reverse()
    stacks = [[] for x in range(stack_count)]
    for repr in stackrepr:
        idx = 0
        for entry in repr:
            if entry:
                stacks[idx].append(entry[0])
            idx += 1
    for line in input:
        line = line.strip()
        if line:
            moves.append(re.findall('\d+', line ))
        else:
            break
# Now run through and execute all the moves
for move in moves:
    (count, fr, to) = [int(x) for x in move]
    for x in range(count):
        stacks[to-1].append(stacks[fr-1].pop())

result = "".join([stack.pop() for stack in stacks])
print(stacks, result)
