forest = []
def get_row(f, row):
    return [int(x) for x in list(f[row])]
def get_col(f, col):
    return [int(tree[col]) for tree in f]
    
def vd(candidate, seq):
    d = 0
    for t in seq:
        d += 1
        if t>=candidate:
            break
    return d
    
def do_score(seq, pos):
    candidate = seq[pos]
    bef = seq[:pos]
    aft = seq[pos+1:]
    bef.reverse()
    score = vd(candidate, bef) * vd(candidate, aft)
    bef.reverse()
    #print(seq, pos, bef, candidate, aft, score)
    return score
    
def score(trees, row, col):
    r = get_row(trees, row)
    c = get_col(trees, col)
    score = do_score(r, col) * do_score(c, row)
    #print("SCORE!",r, c, score)
    return score

with open('input.txt') as input:
    tot = 0
    totmax = 0
    for line in input:
        line = line.strip()
        if line:
            forest.append(line)
v = 0
score_max = 0
for r in range(len(forest)):
    for c in range(len(forest[0])):
        score_max = max(score(forest, r, c), score_max)
print(score_max)