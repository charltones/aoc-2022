import time
rocks = []
with open('input.txt') as input:
    for line in input:
        line = line.strip()
        if line:
            rock = [(int(x), int(y)) for [x, y] in [x.split(',') for x in line.split(' -> ')]]
            rocks.append(rock)
            
minx = rocks[0][0][0]
miny = rocks[0][0][1]
maxx = 0
maxy = 0
# work out size of grid area
for r in rocks:
    for (x, y) in r:
        minx = min(minx, x)
        miny = min(miny, y)
        maxx = max(maxx, x)
        maxy = max(maxy, y)
print("Rock area = (%d, %d) to (%d, %d)" % (minx, miny, maxx, maxy))
# expand playing grid to allow space for sand to fall
miny = 0
maxy += 1
minx -= 200
maxx += 200
offset = minx
grid = [ ['.']*(maxx+1-offset) for i in range(maxy+1)]
# render rock lines into grid
for r in rocks:
    px = py = None
    for (x, y) in r:
        if px:
            print("Draw rock from %d, %d to %d, %d" % (px,py, x,y))
            if px==x:
                for ry in range(min(py,y), max(py,y) + 1):
                    grid[ry][px-offset] = '#'
            elif py==y:
                for rx in range(min(px,x), max(px,x) + 1):
                    grid[py][rx-offset] = '#'
        px = x
        py = y

# simulate falling sand grains
def sand(grid, x, y):
    minx = 0
    maxx = len(grid[0])
    maxy = len(grid)-1
    if y<maxy:
        if grid[y+1][x]=='.':
            # move down
            return sand(grid, x, y+1)
        elif grid[y+1][x-1]=='.':
            # move down-left
            return sand(grid, x-1, y+1)
        elif grid[y+1][x+1]=='.':
            # move down-right
            return sand(grid, x+1, y+1)
        elif grid[y][x]=='o':
            # full
            return (grid, 'end')
        else:
            # come to rest
            grid[y][x] = 'o'
            return (grid, 'flow')
    else:
        # reach abyss
        # come to rest
        grid[y][x] = 'o'
        return (grid, 'flow')

        
unit = 0
result = 'flow'
while result=='flow':
    (grid, result) = sand(grid, 500-offset, 0)
    #print("\033[H\033[J", end="")
    #for r in grid:
    #    print("".join(r))
    #time.sleep(0.1)
    unit += 1
for r in grid:
    print("".join(r))
print("%d units of sand fell" % (unit-1))