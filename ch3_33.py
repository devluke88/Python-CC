things = ['car', 'plane', 'boat', 'spaceship']
for thing in things:
    if thing.startswith('s'):
        print(f"I would like to own an {thing.title()}!")
    else:
        print(f"I would like to own a {thing.title()}!")