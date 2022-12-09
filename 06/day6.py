with open('input.txt') as input:
    f = input.read()
    for w in range(len(f)-3):
        test = f[w:w+4]
        
        if len(set(test)) == 4:
            print(w+4)
            break
