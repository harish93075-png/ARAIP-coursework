GRID_SIZE = 6
robot = [0, 0]
goal = [5, 5]
walls = [[2, 1], [2, 2], [2, 3], [4, 4]]

def show_grid():
       for y in range(GRID_SIZE):
           row = ""
           for x in range(GRID_SIZE):
               if [x, y] == robot:
                   row += "R "
               elif [x, y] == goal:
                   row += "G "
               elif [x, y] in walls:
                   row += "# "
               else:
                   row += ". "
           print(row)
       print()

show_grid()