import numpy as np

grid_game = [[0] * 5] * 5
new_file = [1] * 5
zeros_file = [0] * 5

grid_game.insert(0,new_file)
grid_game.pop(5)


for x in range(0,5):
    grid_game.insert(0, zeros_file)
    grid_game.pop(5)
    print(grid_game)
