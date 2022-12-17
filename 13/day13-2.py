from functools import cmp_to_key

def compareit(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return -1
        elif left==right:
            return 0
        else:
            return 1
            
    elif isinstance(left, list) and isinstance(right, list):
        if left and right:
            lv = left[0]
            rv = right[0]
            res = compareit(lv,rv)
            if res==0:
                return compareit(left[1:], right[1:])
            else:
                return res
        else:
            if not left and not right:
                return 0
            elif not left:
                return -1
            else:
                return 1
                
    else:
        if isinstance(left, int) and isinstance(right, list):
            return compareit([left], right)
        elif isinstance(left, list) and isinstance(right, int):
            return compareit(left, [right])
        else:
            print("I've gone bonkers!", 4/0)

with open('input.txt') as input:
    lines = []
    for line in input:
        line = line.strip()
        
        if line:
            lines.append(eval(line))
        
lines = lines + [[[2]], [[6]]]
print(lines)
lines = sorted(lines, key=cmp_to_key(compareit))
idx1 = lines.index([[2]])+1
idx2 = lines.index([[6]])+1
print(lines)
print(idx1 * idx2)