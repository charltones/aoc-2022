
class Node():
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.cost = 0

    def __eq__(self, other):
        return self.position == other.position
        
    def __repr__(self):
        return "(%d, %d)" % (self.position[0], self.position[1])
        
def djikstra(maze, start, end):
    path = []
    heap = []
    visited = []
    start_node = Node(position=start)
    end_node = Node(position=end)
    heap.append(start_node)
    tot_nodes = len(maze) * len(maze[0])
    while len(heap):
        heap = sorted(heap, key=lambda x: x.cost, reverse=True)
        current = heap.pop()
        visited.append(current)
        print("Visited %d / %d (%.2f%%)" % (len(visited), tot_nodes, 100.0*(len(visited) / tot_nodes)))
        if current==end_node:
            #         Congratz! You've found the end! Backtrack to get path   
            while current:
                path.append(current.position)
                current = current.parent
            return path[::-1]

        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]: # Adjacent squares
            # Get node position
            node_position = (current.position[0] + new_position[0], current.position[1] + new_position[1])
            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[0]) -1) or node_position[1] < 0:
                continue
            # Make sure not more than 1 step up
            cur_height = maze[current.position[0]][current.position[1]]
            new_height = maze[node_position[0]][node_position[1]]
            if ord(new_height) - ord(cur_height) > 1:
                continue
            # Append
            children.append(Node(position=node_position, parent=current))

        for child in children:
            skip = False
            for seen_node in visited:
                if child==seen_node:
                    skip = True
                    break
            if skip:
                continue
            
            child.cost = current.cost + 1

            for heap_node in heap:
                skip = False
                if child==heap_node:
                    skip = True
                    if child.cost < heap_node.cost:
                        heap_node.cost = child.cost
                        heap_node.parent = child.parent
                    break
            if skip:
                continue
            # Add the child to the heap
            heap.append(child)

    return path

# read the maze 
maze = []
with open('input.txt') as input:
    for line in input:
        line = line.strip()
        if line:
            maze.append(list(line))
# find start and end, and print it
for r in range(len(maze)):
    row = maze[r]
    print("".join(row))
    for c in range(len(row)):
        char = row[c]
        if char=='S':
            maze[r][c]='a'
            start = (r, c)
        elif char=='E':
            maze[r][c]='z'
            end = (r, c)
            
print("Start", start)
print("End", end)

path = djikstra(maze, start, end)
print(path)
for (r,c) in path:
    maze[r][c]='.'
for r in range(len(maze)):
    row = maze[r]
    print("".join(row))

print(len(path)-1)