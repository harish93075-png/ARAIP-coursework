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

def move(command):
       dx, dy = 0, 0
       if command == "up":
           dy = -1
       elif command == "down":
           dy = 1
       elif command == "left":
           dx = -1
       elif command == "right":
           dx = 1
       else:
           print("Unknown command. Use up, down, left, right or quit.")
           return
       new_x = robot[0] + dx
       new_y = robot[1] + dy
       if not (0 <= new_x < GRID_SIZE and 0 <= new_y < GRID_SIZE):
           print("Blocked: edge of map")
       elif [new_x, new_y] in walls:
           print("Blocked: wall")
       else:
           robot[0], robot[1] = new_x, new_y

while True:
       show_grid()
       if robot == goal:
           print("Goal reached!")
           break
       command = input("Command (up/down/left/right/quit): ").strip().lower()
       if command == "quit":
           break
       move(command)
