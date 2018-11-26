import random
import os


from CrackerBarrelTriangle import CrackerBarrelTriangle


def get_random_solution(triangle: CrackerBarrelTriangle):

    def inner_get_random_solution(triangle: CrackerBarrelTriangle, seq: list):
        if triangle.get_num_pegs() == 1:
            return seq
        for hole in triangle.get_hole_locations():
            directions = triangle.get_possible_jumps(*hole)  # ordered
            random.shuffle(directions)                       # unordered
            for direction in directions:
                new_jump = (hole, direction)
                new_triangle = triangle.clone()
                new_triangle.jump_pegs(*new_jump)
                new_seq = seq.copy()
                new_seq.append(new_triangle)
                i = inner_get_random_solution(new_triangle, new_seq)
                if i:
                    return i
        # If we've reached this point, dead end
        return None

    return inner_get_random_solution(triangle, [triangle])


def print_seq(seq: list, print_width: int):
    triangle_height, max_triangle_width = 7, 15
    max_triangles_per_line = print_width // (max_triangle_width+1)
    padded_triangle_lists = []
    for triangle in seq:
        triangle_lines = str(triangle).split('\n')
        padded_lines = []
        for line in triangle_lines:
            line = line.replace('\n', '')
            while len(line) < max_triangle_width+1:
                line += ' '
            line += '\n'
            padded_lines.append(line)
        padded_triangle_lists.append(padded_lines)
    for l in range(0, len(padded_triangle_lists), max_triangles_per_line):
        u = l+max_triangles_per_line
        t_str = ''
        for i in range(triangle_height):
            for triangle_lines in padded_triangle_lists[l:u]:
                triangle_lines = triangle_lines
                t_str += triangle_lines[i].replace('\n', '')
            t_str += '\n'
        print(t_str)


if __name__ == '__main__':
    # setup
    i = random.randint(0, 4)
    j = random.randint(0, i)
    initial_triangle = CrackerBarrelTriangle(remove_peg=(i, j))
    terminal_width = int(os.popen('tput cols').read().replace('\n', ''))

    # execution of algorithm on input space
    solution_sequence = get_random_solution(initial_triangle)
    print()
    print_seq(solution_sequence, terminal_width)
