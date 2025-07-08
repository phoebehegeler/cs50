# Mars Rover Mapping
#### Video Demo: [Project](https://youtu.be/N_Hd6mTGTZA)
#### Description:
#### My final project is a Mars Rover Mapping Simulation made using python and can be seen in the terminal. The user has to option to move the Rover forward, backward, left or right and then to view the map on a 2D grid and see the coordinates of the Rover and its direction. The program has a main function and 6 other functions which are move_rover, forward, backward, left, right, and show_map.

#### A 10x10 grid is created as a representation of the Martian terrain. The Rover starts initially at position at 0,0 facing North. The user has the ability to move the Rover throughout the grid by entering F for forwards, B for backwards, L for turning to the left and R for turning to the right. L and R only rotate the Rover and then they can be moved by entering F or B after the rotation.


#### Main Function
#### The main function initializes the grid and sets up the initial position and direction of the Rover. Then it enters a loop asking user input commands. Depending on the user’s command, the program either moves the Rover or displays the map. The main function also prints out the Rover's position and direction before and after each command. If the user enters Q, the function quits the program.

#### move_rover Function: The move_rover function executes the user’s movement commands. It checks if the user has inputed a command to move forward, backward, or rotate the Rover, and then calls the function accordingly. It also marks the current position as "visited" on the grid.. This function returns the updated position and direction of the Rover, reflecting its new state after each move.

#### forward Function: The forward function handles the logic for moving the Rover one step forward in the direction it is currently facing. If the Rover is facing North or South, the y-coordinate increases or decreases respectively. If the Rover is facing East or West, the x-coordinate increases or decreases respectively. The function makes sure the Rover stays inside the grid's boundaries.

#### backward Function: The backward function handles the logic for moving the Rover one step backward in the direction it is currently facing. If the Rover is facing North or South, the y-coordinate decreases or increases respectively. If the Rover is facing East or West, the x-coordinate decreases or increases respectively. The function makes sure the Rover stays inside the grid's boundaries.

#### left and right Functions: The left function rotates the Rover 90 degrees to the left, while the right function rotates it 90 degrees to the right. These functions do not change the Rover's position but change its direction.

### show_map Function: The show_map function visually represents the grid and the Rover's position. It prints out a map where R represents the Rover’s current location, a period (.) represents the positions the Rover has visited, and # represents the unavigated areas.

### The reason I chose this as my project is because I have always been interested in aerospace engineering - particularly the computer science aspect of it - and I wrote an essay about the SLAM technology used in the Mars Ingenuity Helicopter. Therefore, I chose to make a simple project with a Map of a Mars Rover and its position and direction to mildly reference that.
