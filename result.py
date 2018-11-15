final_result = [233526, 821847, 1361058, 641612, 61650, 4008, 1268, 5, 0, 2, 0, 0, 0, 0, 0]
final_result_sum = sum(final_result)

print('There are {} possible outcomes of that game on the counter in Cracker Barrel'
        .format(final_result_sum))
print('{}% chance of leaving 1 peg'
        .format(int((final_result[0]/final_result_sum)*100)))
print('{}% chance of leaving 2 pegs'
        .format(int((final_result[1]/final_result_sum)*100)))
print('{}% chance of leaving 3 pegs'
        .format(int((final_result[2]/final_result_sum)*100)))
print('{}% chance of leaving 4 or more pegs'
        .format(int((sum(final_result[3:])/final_result_sum)*100)))
