def points(games):
    x, y = [], []
    points_sum = 0
    for game in games:
        match = game.split(":", 1)
        x = int(match[0])
        y = int(match[1])
        if x > y:
            points_sum += 3
        elif x == y:
            points_sum += 1
        else:
            points_sum += 0
    return points_sum

games = ['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3']
test = points(games)
print(test)