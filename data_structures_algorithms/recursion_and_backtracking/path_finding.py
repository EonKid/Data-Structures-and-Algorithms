"""
Path Finding Problem
Given an N×N matrix of blocks with a source upper left block, we want to find a path from the source to the destination(the lower right block). We can only move downwards and to the left. Also a path is given by 1
1 and a wall is given by 0

Maze = [[ 1 , 0 , 0 , 0 ],
[ 1 , 1 , 0 , 0 ],
[ 0 , 1 , 0 , 0 ],
[ 0 , 1 , 1 , 1 ]]
Find path from (0,0) to (3,3)
Solution: (0,0)→(1,0)→(1,1)→(2,1)→(3,1)→(3,2)→(3,3)

Maze = [[ 1 , 0 , 1, 0 , 0],
        [ 1 , 1 , 0, 1 , 0],
        [ 0 , 1 , 0, 1 , 0],
        [ 0 , 1 , 0, 0 , 0],
        [ 1 , 1 , 1, 1 , 1]
        ]
Find path from (0,0) to (5,5)
(0, 0), (1, 0), (1, 1), (2, 1), (3, 1), (4, 1), (4, 2), (4, 3), (4, 4)
"""


def solveMaze(maze, position, N):
    if position == (N - 1, N - 1):
        return [(N - 1, N - 1)]
    x, y = position
    if x + 1 < N and maze[x + 1][y] == 1:
        a = solveMaze(maze, (x + 1, y), N)
        if a != None:
            return [(x, y)] + a

    if y + 1 < N and maze[x][y + 1] == 1:
        b = solveMaze(maze, (x, y + 1), N)
        if b != None:
            return [(x, y)] + b


Maze = [
        [ 1 , 0 , 0 , 0 ],
        [ 1 , 1 , 0 , 0 ],
        [ 0 , 1 , 0 , 0 ],
        [ 0 , 1 , 1 , 1 ]
        ]
print(solveMaze(Maze, (0, 0), len(Maze)))
