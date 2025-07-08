import unittest
from mars_rover import move_rover,forward,backward,left,right

class TestMarsRover(unittest.TestCase):

    def test_forward_north(self):
        position= [0, 0]
        direction= "N"
        grid_size= 10
        expected_position= [0, 1]
        new_position= forward(position, direction, grid_size)
        self.assertEqual(new_position, expected_position)

    def test_forward_south(self):
        position= [0, 1]
        direction= "S"
        grid_size= 10
        expected_position= [0, 0]
        new_position= forward(position, direction, grid_size)
        self.assertEqual(new_position, expected_position)

    def test_forward_east(self):
        position= [0, 0]
        direction= "E"
        grid_size= 10
        expected_position= [1, 0]
        new_position= forward(position, direction, grid_size)
        self.assertEqual(new_position, expected_position)

    def test_forward_west(self):
        position= [1, 0]
        direction= "W"
        grid_size= 10
        expected_position= [0, 0]
        new_position= forward(position, direction, grid_size)
        self.assertEqual(new_position, expected_position)

    def test_backward_north(self):
        position= [0, 1]
        direction= "N"
        grid_size= 10
        expected_position= [0, 0]
        new_position= backward(position, direction, grid_size)
        self.assertEqual(new_position, expected_position)

    def test_backward_south(self):
        position= [0, 0]
        direction= "S"
        grid_size= 10
        expected_position= [0, 1]
        new_position= backward(position, direction, grid_size)
        self.assertEqual(new_position, expected_position)

    def test_turn_left(self):
        direction= "N"
        expected_direction= "E"
        new_direction= left(direction)
        self.assertEqual(new_direction, expected_direction)

    def test_turn_right(self):
        direction= "N"
        expected_direction= "E"
        new_direction= right(direction)
        self.assertEqual(new_direction, expected_direction)

    def test_map_update(self):
        grid_size= 10
        position= [0, 0]
        visited= [[0 for _ in range(grid_size)] for _ in range(grid_size)]
        visited[position[1]][position[0]] = 1
        expected_visited= visited.copy()
        expected_visited[1][0]= 1
        new_position, direction= move_rover("F", position, "N", grid_size, visited)
        self.assertEqual(visited, expected_visited)

if __name__ == '__main__':
    unittest.main()
