monkeys = []
with open('input.txt') as input:
    for line in input:
        line = line.strip()
        if line:
            match = line[:5]
            if match=='Monke':
                num = [int(s) for s in line.split()[1].split(':') if s.isdigit()][0]
                print("Parsing Monkey #", num)
                monkey = {'id':int(num), 'inspects':0}
                monkeys.append(monkey)
            elif match=='Start':
                monkey['items'] = [int(x) for x in line.split(': ')[1].split(', ')]
            elif match=='Opera':
                monkey['operation'] = line.split('= ')[1]
            elif match=='Test:':
                monkey['test'] = [int(s) for s in line.split() if s.isdigit()][0]
            elif match=='If tr':
                monkey['if_t'] = [int(s) for s in line.split() if s.isdigit()][0]
            elif match=='If fa':
                monkey['if_f'] = [int(s) for s in line.split() if s.isdigit()][0]
            else:
                print("PARSE ERROR!")
for round in range(1,21):
    for monkey in monkeys:
        for old in monkey['items']:
            monkey['inspects'] = monkey['inspects'] + 1
            print("Round %d monkey %d inspects item %d" % (round, monkey['id'], old))
            new = eval(monkey['operation'])
            print("  worry level is '%s' to %d" % (monkey['operation'], new))
            new = new // 3
            print("  monkey gets bored of item so worry level is %d" % (new))
            if new % monkey['test'] == 0:
                print("  worry %d is divisible by %s so monkey throws %d to %d" % (new, monkey['test'], new, monkey['if_t']))
                monkeys[monkey['if_t']]['items'].append(new)
            else:
                print("  worry %d is NOT divisible by %s so monkey throws %d to %d" % (new, monkey['test'], new, monkey['if_f']))
                monkeys[monkey['if_f']]['items'].append(new)
        monkey['items'] = []
    print("After round %d:" % (round))
    for monkey in monkeys:
        print("Monkey %d: Items:" % (monkey['id']), monkey['items'])
print("After round 20:")
mb = []
for monkey in monkeys:
    print("Monkey %d: inspected %d items" % (monkey['id'], monkey['inspects']))
    mb.append(monkey['inspects'])
    
mb.sort()
print(mb)

monkey_business = mb.pop() * mb.pop()
print (monkey_business)
