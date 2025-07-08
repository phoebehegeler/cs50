#i am interested in aerospace engineering and i did an essay on the the mapping of the SLAM technology so for fun i have coded 'the mars rover'
#  but it could be any vehicle moving front, back, left and right

def main():
    grid_size = 10
    position = [0, 0]
    direction = "N"
    visited = [[0 for _ in range(grid_size)] for _ in range(grid_size)] #2d grid
    visited[position[1]][position[0]] = 1

    while True:
        command= input("Enter commands for the Mars Rover (F is forward, B is backward, L is left, R is right, M is to show the map, Q is to quit): ").upper()
        if command=="Q":
            break
        print(f"Before move: Position: {position}, Direction: {direction}")
        if command =="M":
            show_map(visited, position)
        else:
            position,direction = move_rover(command,position,direction, grid_size, visited)
        print(f"After move: Position: {position}, Direction: {direction}")
    print(f"Final Rover position: {position}, Facing: {direction}")

def move_rover(command,position,direction,grid_size,visited):
    new_position = position.copy()
    if command== "F":
        new_position= forward(position,direction,grid_size)
    elif command == "B":
        new_position = backward(position,direction,grid_size)
    elif command == "L":
        direction = left(direction)
    elif command== "R":
        direction= right(direction)
    if new_position!= position:
        visited[new_position[1]][new_position[0]]= 1
    return new_position, direction

def forward(position,direction,grid_size):
    new_position = position.copy()
    if direction== "N" and position[1] <grid_size- 1:
        new_position[1]+= 1
    elif direction== "S" and position[1]> 0:
        new_position[1]-= 1
    elif direction== "E" and position[0]< grid_size - 1:
        new_position[0]+= 1
    elif direction== "W" and position[0]> 0:
        new_position[0]-= 1
    return new_position

def backward(position, direction, grid_size):
    new_position= position.copy()
    if direction== "N" and position[1] >0:
        new_position[1]-= 1
    elif direction== "S" and position[1]< grid_size- 1:
        new_position[1]+= 1
    elif direction== "E" and position[0]> 0:
        new_position[0]-= 1
    elif direction== "W" and position[0]< grid_size - 1:
        new_position[0]+= 1
    return new_position

def left(direction):
    directions =["N","E","S","W"]
    new_index= (directions.index(direction) +1) % 4
    return directions[new_index]

def right(direction):
    directions= ["N","E","S","W"]
    new_index= (directions.index(direction)+1)%4
    return directions[new_index]

def show_map(visited, position):
    print("\nMap of the Rover's Exploration:")
    for y in range(len(visited)-1,-1,-1):
        row= ""
        for x in range(len(visited[y])):
            if [x,y]== position:
                row += "R "
            elif visited[y][x]== 1:
                row+= ". "
            else:
                row+= "# "
        print(row)
    print()

if __name__ == "__main__":
    main()
