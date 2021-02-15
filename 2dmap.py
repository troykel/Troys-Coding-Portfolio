
import random
import numpy as np
"""Objective: To plot 2 p's among the 23 x's and determine how
many moves it would take to go from p1 to p2"""
listx = ["x" for i in range(25)]
p1 = 'p1'
p2 = 'p2'
random_index = random.randrange(len(listx))
listx[random_index] = p1
random_index = random.randrange(len(listx))
listx[random_index] = p2
print(listx)
twodim = np.array(listx).reshape(-1, 5)
print(twodim)
for row in range(5):
    for col in range(5):
        if twodim[row][col] == "p1":
            row1, col1 = row, col
        if twodim[row][col] == "p2":
            row2, col2 = row, col
moves = abs(row2 - row1) + abs(col2 - col1)
print(f"Number of moves = {moves}")















