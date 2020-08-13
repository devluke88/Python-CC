# Automate Python Exercise - character picture grid p.103

grid = [['.', '.', '.', '.', '.', '.'], 
        ['.', 'O', 'O', '.', '.', '.'], 
        ['O', 'O', 'O', 'O', '.', '.'], 
        ['O', 'O', 'O', 'O', 'O', '.'], 
        ['.', 'O', 'O', 'O', 'O', 'O'], 
        ['O', 'O', 'O', 'O', 'O', '.'], 
        ['O', 'O', 'O', 'O', '.', '.'], 
        ['.', 'O', 'O', '.', '.', '.'], 
        ['.', '.', '.', '.', '.', '.']]

def image(grid):
    x, y = len(grid) - 1, len(grid[0]) - 1
    for i in range(0, y+1):
        for j in range(0,x+1):
            print(grid[j][i], end="")
        print("")
    return x,y

print(image(grid))
