with open('input.txt') as input:
    f = input.read()
    for w in range(len(f)-13):
        test = f[w:w+14]
        
        if len(set(test)) == 14:
            print(w+14)
            break
