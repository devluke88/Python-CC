def guess_blue(blue_start, red_start, blue_pulled, red_pulled):
    return float((blue_start - blue_pulled) / ((blue_start- blue_pulled) + (red_start - red_pulled)))


test = guess_blue(5, 5, 2, 3)
print(test)