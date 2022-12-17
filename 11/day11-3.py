monkeys = []
with open('input2.txt') as input:
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
                monkey['operation'] = line.split('= ')[1].split()
            elif match=='Test:':
                monkey['test'] = [int(s) for s in line.split() if s.isdigit()][0]
            elif match=='If tr':
                monkey['if_t'] = [int(s) for s in line.split() if s.isdigit()][0]
            elif match=='If fa':
                monkey['if_f'] = [int(s) for s in line.split() if s.isdigit()][0]
            else:
                print("PARSE ERROR!")
for round in range(1,10001):
    for monkey in monkeys:
        for old in monkey['items']:
            monkey['inspects'] = monkey['inspects'] + 1
            v1 = old
            op = monkey['operation'][1]
            v2 = monkey['operation'][2]
            if v2=='old':
                v2 = old
            else:
                v2 = int(v2)
            if op=='+':
                new = v1 + v2
            elif op=='-':
                new = v1 - v2
            elif op =='*':
                new = v1 * v2
            if new % monkey['test'] == 0:
                monkeys[monkey['if_t']]['items'].append(new)
            else:
                monkeys[monkey['if_f']]['items'].append(new)
        monkey['items'] = []
    if round % 100 == 0:
        print("After round %d:" % (round))
        for monkey in monkeys:
            print("Monkey %d: Items:" % (monkey['id']), monkey['items'])
print("After round 10000:")
mb = []
for monkey in monkeys:
    print("Monkey %d: inspected %d items" % (monkey['id'], monkey['inspects']))
    mb.append(monkey['inspects'])
    
mb.sort()
print(mb)

monkey_business = mb.pop() * mb.pop()
print (monkey_business)
