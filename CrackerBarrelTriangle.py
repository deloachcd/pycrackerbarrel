import numpy as np
from copy import deepcopy

# Simple function for determining if location is within triangle
position_in_triangle = lambda i,j: (j <= i and i < 5 and j < 5
                                        and i >= 0 and j >= 0)

# Peg positions used for making jumps, relative to a hole
peg_positions = {
        'up':                   lambda i,j: ((i-1,j),(i-2,j)),
        'diagonal_up_right':    lambda i,j: ((i-1,j+1),(i-2,j+2)),
        'right':                lambda i,j: ((i,j+1),(i,j+2)),
        'diagonal_down_right':  lambda i,j: ((i+1,j+1),(i+2,j+2)),
        'down':                 lambda i,j: ((i+1,j),(i+2,j)),
        'diagonal_down_left':   lambda i,j: ((i+1,j-1),(i+2,j-2)),
        'left':                 lambda i,j: ((i,j-1),(i,j-2)),
        'diagonal_up_left':     lambda i,j: ((i-1,j-1),(i-2,j-2)),
}

class CrackerBarrelTriangle:
    ''' Class to represent one of those triangles with pegs that you
        find in cracker barrel restaurants. '''

    def __init__(self,**kwargs):
        ''' "1" specifies peg, while "0" specifies hole '''
        self.internal_representation = np.array([[1],
                                                 [1,1],
                                                 [1,1,1],
                                                 [1,1,1,1],
                                                 [1,1,1,1,1]])
        if 'remove_peg' in kwargs.keys():
            r = kwargs['remove_peg']
            if not position_in_triangle(*r):
                raise Exception("Invalid hole specified for initial peg removal")
            else:
                self.remove_peg(*r)

    def get_hole_locations(self):
        holes = []
        for i,row in enumerate(self.internal_representation):
            for j,value in enumerate(row):
                if value == 0:
                    holes.append((i,j))
        return holes

    def get_possible_jumps(self,i,j):
        possible_directions = []
        for direction,positions in peg_positions.items():
            relative_positions = positions(i,j)
            p1,p2 = relative_positions[0],relative_positions[1]
            if (position_in_triangle(*p1) and position_in_triangle(*p2)
                    and self.peg_present(*p1) and self.peg_present(*p2)):
                possible_directions.append(direction)
        return possible_directions

    def jump_pegs(self,source_hole:tuple,direction:str):
        jump_positions = peg_positions[direction](*source_hole)
        jumped_peg,jumping_peg = jump_positions[0], jump_positions[1]
        if (position_in_triangle(*source_hole) and
                position_in_triangle(*jump_positions[0]) and
                position_in_triangle(*jump_positions[1]) and
                not self.peg_present(*source_hole) and
                self.peg_present(*jumped_peg) and
                self.peg_present(*jumping_peg)):
            self.place_peg(*source_hole)
            self.remove_peg(*jumped_peg)
            self.remove_peg(*jumping_peg)
        else:
            raise Exception('Invalid jump requested')

    def peg_present(self,i,j):
        if position_in_triangle(i,j):
            return self.internal_representation[i][j] == 1
        else:
            raise Exception('Checked for peg presence in location not in triangle')
    
    def remove_peg(self,i,j):
        if position_in_triangle(i,j):
            self.internal_representation[i][j] = 0
        else:
            raise Exception('Requested peg removal for location not in triangle')

    def place_peg(self,i,j):
        if position_in_triangle(i,j):
            self.internal_representation[i][j] = 1
        else:
            raise Exception('Requested peg placement for location not in triangle')

    def clone(self):
        return deepcopy(self)

    def get_num_pegs(self):
        return 15 - len(self.get_hole_locations())

    def __str__(self):
        rep_str = ''
        for i,row in enumerate(self.internal_representation):
            for peg in row:
                rep_str += str(peg)
            if i < 4:
                rep_str += '\n'
        return rep_str

    def __repr__(self):
        rep_str = 'Triangle('
        for i,row in enumerate(self.internal_representation):
            for peg in row:
                rep_str += str(peg)
            if i < 4:
                rep_str += ','
        rep_str += ')'
        return rep_str
