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

with open('input2.txt') as input:
    left = right = None
    i = 1
    correct = []
    for line in input:
        line = line.strip()
        
        if line:
            if not left:
                left = line
            else:
                right = line
                result = compareit(eval(left), eval(right))
                print("Pair %d, Left = %s, right=%s, correct=%s" % (i, left, right, result))
                if result==-1:
                    correct.append(i)
                i += 1
                left = None
                right = None
        
print(correct, sum(correct))