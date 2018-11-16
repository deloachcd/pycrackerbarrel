import unittest
import numpy as np

from CrackerBarrelTriangle import CrackerBarrelTriangle

class TestCrackerBarrelTriangle(unittest.TestCase):

    def test__init__(self):
        # Test 'standard' init works
        CrackerBarrelTriangle()
        
        # Test init with a valid peg removed
        CrackerBarrelTriangle(remove_peg=(2,1))
        
        # Test init with invalid pegs specified for removal
        self.assertRaises(Exception, lambda: CrackerBarrelTriangle(remove_peg=(1,4)))
        self.assertRaises(Exception, lambda: CrackerBarrelTriangle(remove_peg=(5,5)))

    def test_get_hole_locations(self):
        # Test that we detect all the holes we expect
        t = CrackerBarrelTriangle()
        t.internal_representation = np.array([[0],
                                              [0,1],
                                              [1,0,1],
                                              [1,1,1,0],
                                              [0,1,0,0,1]])
        expected_locations = [(0,0),(1,0),(2,1),(3,3),(4,0),(4,2),(4,3)]
        hole_locations = t.get_hole_locations()
        # All holes returned are in expected locations
        for hole_location in hole_locations:
            self.assertIn(hole_location, expected_locations)
        # All expected locations are returned
        for expected_location in expected_locations:
            self.assertIn(expected_location, hole_locations)
        
        # By default, CrackerBarrelTriangle initialized with no holes
        t = CrackerBarrelTriangle()
        self.assertEqual(t.get_hole_locations(),[])

    def test_get_possible_jumps(self):
        def assertDirectionsEqual():
            for expected_direction in expected_directions:
                self.assertIn(expected_direction, returned_directions)
            for returned_direction in returned_directions:
                self.assertIn(returned_direction, expected_directions)

        t = CrackerBarrelTriangle()
        
        # Make sure we don't return jumps possible
        # if we have a peg in hole_location
        self.assertEqual(t.get_possible_jumps(0,0),[])

        # Directional validity checks
        t.remove_peg(0,0)
        returned_directions = t.get_possible_jumps(0,0)
        expected_directions = ['down', 'diagonal_down_right']
        assertDirectionsEqual()
        t.place_peg(0,0)
        
        t.remove_peg(2,0)
        returned_directions = t.get_possible_jumps(2,0)
        expected_directions = ['down', 'up', 'right', 'diagonal_down_right']
        assertDirectionsEqual()
        t.place_peg(2,0)

        t.remove_peg(2,2)
        returned_directions = t.get_possible_jumps(2,2)
        expected_directions = ['left', 'diagonal_down_left', 'down',
                               'diagonal_down_right', 'diagonal_up_left']
        assertDirectionsEqual()
        t.place_peg(2,2)

        t.remove_peg(4,0)
        returned_directions = t.get_possible_jumps(4,0)
        expected_directions = ['up', 'diagonal_up_right', 'right']
        assertDirectionsEqual()
        t.place_peg(4,0)

        t.remove_peg(4,4)
        returned_directions = t.get_possible_jumps(4,4)
        expected_directions = ['diagonal_up_left', 'left']
        assertDirectionsEqual()
        t.place_peg(4,4)

        # Set up for next two tests
        t.remove_peg(0,0)

        # Check to make sure no jumps possible if no
        # pegs within 1-peg distance of hole
        t.remove_peg(1,0)
        t.remove_peg(1,1)
        self.assertEqual(t.get_possible_jumps(0,0),[])

        # Check to make sure no jumps possible if no
        # pegs within 2-peg distance of hole
        t.place_peg(1,0)
        t.remove_peg(2,0)
        self.assertEqual(t.get_possible_jumps(0,0),[])

    def test_jump_pegs(self):
        def assertJump(tri, p0, p1, p2):
            self.assertEqual(tri[p0[0]][p0[1]], 1)
            self.assertEqual(tri[p1[0]][p1[1]], 0)
            self.assertEqual(tri[p2[0]][p2[1]], 0)
        
        t = CrackerBarrelTriangle(remove_peg=(0,0))
        ti = t.internal_representation
        t.jump_pegs((0,0),'down')
        assertJump(ti,(0,0),(1,0),(2,0))

        t = CrackerBarrelTriangle(remove_peg=(0,0))
        ti = t.internal_representation
        t.jump_pegs((0,0),'diagonal_down_right')
        assertJump(ti,(0,0),(1,1),(2,2))

        t = CrackerBarrelTriangle()
        self.assertRaises(Exception, lambda: t.jump_pegs((0,0),'down'))
        self.assertRaises(Exception, lambda: t.jump_pegs((6,6),'up'))
        t.remove_peg(0,0)
        self.assertRaises(Exception, lambda: t.jump_pegs((0,0),'up'))
