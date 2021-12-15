level2sg =[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 7, 0, 0, 0, 
0, 0], [0, 0, 0, 0, 7, 1, 7, 0, 0, 0, 0], [0, 0, 0, 7, 1, 1, 1, 7, 0, 0, 0 
], [0, 0, 7, 1, 1, 1, 1, 1, 7, 0, 0], [0, 7, 1, 1, 1, 1, 1, 1, 1, 7, 0], [ 
0, 0, 7, 1, 1, 1, 1, 1, 7, 0, 0], [0, 0, 0, 7, 1, 1, 1, 7, 0, 0, 0], [0, 0 
, 0, 0, 7, 1, 7, 0, 0, 0, 0], [0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0], [0, 0, 0, 
0, 0, 0, 0, 0, 0, 0, 0]]

def printMatrix():
    i = 0
    while i  < len(level2sg):
        print(level2sg[i])
        i += 1
    
while True:
    countOfSeven = 16
    #printMatrix() if You want to see your progress
    x,y = input('enter dimensions (x,y). Separate by comma : ').split(',')
    x = int(x)
    y = int(y)
    if level2sg[x][y] == 7 or 0:
        level2sg[x][y] = 2
        countOfSeven -= 1
        
    elif level2sg[x][y] == 1:
        print('You lost the game, bye.')
    elif countOfSeven == 0:
        print('You Win!!')
        