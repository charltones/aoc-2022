def fast_eval(old, operation):
    op = operation[0]
    v2 = operation[1]
    if v2=='old':
        v2 = old
    else:
        v2 = int(v2)
    if op=='+':
        new = old + v2
    elif op =='*':
        new = old * v2
    return new

monkeys = []
modulo = 1
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
                monkey['operation'] = tuple(line.split('= ')[1].split()[1:])
            elif match=='Test:':
                monkey['test'] = [int(s) for s in line.split() if s.isdigit()][0]
                modulo = modulo * monkey["test"]
            elif match=='If tr':
                monkey['if_t'] = [int(s) for s in line.split() if s.isdigit()][0]
            elif match=='If fa':
                monkey['if_f'] = [int(s) for s in line.split() if s.isdigit()][0]
            else:
                print("PARSE ERROR!")
for round in range(1,10001):
    for monkey in monkeys:
        for item in monkey['items']:
            monkey['inspects'] = monkey['inspects'] + 1
            new = fast_eval(item, monkey['operation']) % modulo
            if new % monkey['test'] == 0:
                monkeys[monkey['if_t']]['items'].append(new)
            else:
                monkeys[monkey['if_f']]['items'].append(new)
        monkey['items'] = []
    if round % 100 == 0:
        print("After round %d:" % (round))
        for monkey in monkeys:
            print("Monkey %d: Items:" % (monkey['id']), len(monkey['items']))
print("After round 10000:")
mb = []
for monkey in monkeys:
    print("Monkey %d: inspected %d items" % (monkey['id'], monkey['inspects']))
    mb.append(monkey['inspects'])
    
mb.sort()
print(mb)

monkey_business = mb.pop() * mb.pop()
print (monkey_business)
