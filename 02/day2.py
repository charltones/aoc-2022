rock = 1
paper = 2
scissors = 3
win = 6
draw = 3
lose = 0
total = 0
score = {
    'A': {
        'X': rock + draw,
        'Y': paper + win,
        'Z': scissors + lose
            
    },
    'B': {
        'X': rock + lose,
        'Y': paper + draw,
        'Z': scissors + win
            
    },
    'C': {
        'X': rock + win,
        'Y': paper + lose,
        'Z': scissors + draw
    },
}
with open('input.txt') as input:
    for line in input:
        line = line.strip()
        play = line[0]
        response = line[2]
        total += score[play][response]
print(total)        
