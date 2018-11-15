from CrackerBarrelTriangle import CrackerBarrelTriangle
from borderprint.borderprint import bordered_print

global_count = [ 0 for i in range(15) ] # global variable

def get_jump_sequences(triangle:CrackerBarrelTriangle):
    global global_count

    jumps_possible = False
    for hole in triangle.get_hole_locations():
        for direction in triangle.get_possible_jumps(*hole):
            jumps_possible = True
            new_jump = (hole,direction)
            new_triangle = triangle.clone()
            new_triangle.jump_pegs(*new_jump)
            get_jump_sequences(new_triangle)
    if not jumps_possible:
        global_count[triangle.get_num_pegs()-1] += 1
        print(global_count)

if __name__ == '__main__':
    # setup
    initial_peg_removals = [(0,0),(1,0),(2,0),(2,1)]
    initial_triangles = [ CrackerBarrelTriangle(remove_peg=peg)
                            for peg in initial_peg_removals ]

    # execution of algorithm on input space
    for triangle in initial_triangles:
        get_jump_sequences(triangle)
    
    # reporting of results
    final_result = global_count
    final_result_sum = sum(final_result)

    bordered_print('FINAL RESULT')
    print('There are {} possible outcomes of that game on the counter in Cracker Barrel.'
            .format(final_result_sum))

    bordered_print('OUTCOMES BY FINAL NUMBER OF PEGS')
    print('{} possible sequences leave 1 peg'.format(final_result[0]))
    print('{} possible sequences leave 2 pegs'.format(final_result[1]))
    print('{} possible sequences leave 3 pegs'.format(final_result[2]))
    print('{} possible sequences leave 4 or more pegs'.format(sum(final_result[3:])))

    bordered_print('CHANCES OF LEAVING N PEGS (assuming random jumps)')
    print('{}% chance of leaving 1 peg'
            .format(int((final_result[0]/final_result_sum)*100)))
    print('{}% chance of leaving 2 pegs'
            .format(int((final_result[1]/final_result_sum)*100)))
    print('{}% chance of leaving 3 pegs'
            .format(int((final_result[2]/final_result_sum)*100)))
    print('{}% chance of leaving 4 or more pegs'
            .format(int((sum(final_result[3:])/final_result_sum)*100)))
