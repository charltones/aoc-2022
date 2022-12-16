
class Node():
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position
        
    def __repr__(self):
        return "(%d, %d)" % (self.position[0], self.position[1])
        
def astar(maze, start, end):
    path = []
    open_list = []
    closed_list = []
    start_node = Node(position=start)
    end_node = Node(position=end)
    open_list.append(start_node)
    while len(open_list):
        open_list = sorted(open_list, key=lambda x: x.f, reverse=True)
        current = open_list.pop()
        closed_list.append(current)
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
            for closed_node in closed_list:
                if child==closed_node:
                    skip = True
                    break
            if skip:
                continue
            
            # Create the f, g, and h values
            child.g = current.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node:
                    skip = True
                    # faster route to same node, copy this node's details into the open list copy
                    if child.g < open_node.g:
                        open_node.g = child.g
                        open_node.f = child.f
                        open_node.parent = child.parent
                    break
            if skip:
                continue
            
            # Add the child to the open list
            open_list.append(child)

    return path

# read the maze 
maze = []
with open('input2.txt') as input:
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

path = astar(maze, start, end)
print(path)
for (r,c) in path:
    maze[r][c]='.'
for r in range(len(maze)):
    row = maze[r]
    print("".join(row))

print(len(path)-1)