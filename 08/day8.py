forest = []
def get_row(f, row):
    return [int(x) for x in list(f[row])]
def get_col(f, col):
    return [int(tree[col]) for tree in f]
def do_visible(seq, pos):
    candidate = seq[pos]
    bef = seq[:pos]
    aft = seq[pos+1:]
    visible = not bef or not aft or max(bef)<candidate or max(aft)<candidate
    #print(seq, pos, bef, candidate, aft, visible)
    return visible
    
def visible(trees, row, col):
    r = get_row(trees, row)
    c = get_col(trees, col)
    return do_visible(r, col) or do_visible(c, row)

with open('input.txt') as input:
    tot = 0
    totmax = 0
    for line in input:
        line = line.strip()
        if line:
            forest.append(line)
for r in forest:
    print(r)
v = 0
for r in range(len(forest)):
    for c in range(len(forest[0])):
        if visible(forest, r, c):
            v += 1
print(v)