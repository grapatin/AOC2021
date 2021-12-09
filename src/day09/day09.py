"""
Template code
"""#import cmath for complex number operations
#from abc import abstractproperty
#import cmath
#import Path for file operations
from pathlib import Path

PROGBLEM_INPUT_TXT = Path("/Users/pergrapatin/Source/AOC2021/src/"\
    +"day09/input.txt").read_text()

EXAMPLE_INPUT1 = """2199943210
3987894921
9856789892
8767896789
9899965678"""
EXAMPLE_RESULT1 = 15

def string_worker(input_string):
    """Helper string worker function
    """
    a_steps = input_string.split("\n")
    a_steps = [int(number) for number in input_string.split(',')]

    return a_steps

def problem_a(input_string, expected_result):
    """Problem A solved function
    """
    row_id = 0
    solution = 0
    storage_dict = {}
    for row in input_string.split('\n'):
        pos_id = 0
        for char in row:
            storage_dict[str(pos_id)+'x'+str(row_id)] = int(char)
            pos_id += 1
        row_id += 1

    row_id = 0
    for row in input_string.split('\n'):
        pos_id = 0
        for char in row:
            current = int(char)
            if str(pos_id-1)+'x'+str(row_id) in storage_dict:
                left = storage_dict[str(pos_id-1)+'x'+str(row_id)]
            else:
                left = 99

            if str(pos_id+1)+'x'+str(row_id) in storage_dict:
                right = storage_dict[str(pos_id+1)+'x'+str(row_id)]
            else:
                right = 99

            if str(pos_id)+'x'+str(row_id-1) in storage_dict:
                up = storage_dict[str(pos_id)+'x'+str(row_id-1)]
            else:
                up = 99

            if str(pos_id)+'x'+str(row_id+1) in storage_dict:
                down = storage_dict[str(pos_id)+'x'+str(row_id+1)]
            else:
                down = 99

            if (current < left) and (current < right) and (current < up) and current < down:
                solution += current + 1
     
            pos_id += 1
        row_id += 1
    

    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

problem_a(EXAMPLE_INPUT1, EXAMPLE_RESULT1)
problem_a(PROGBLEM_INPUT_TXT, 478)
print("\n")

def recursive_mover(pos_x, pos_y, storage_dict, visited_dict):
    counter = 0
    

    current = str(pos_x)+'x'+str(pos_y)

    pos_string_left = str(pos_x-1)+'x'+str(pos_y)
    pos_string_right = str(pos_x+1)+'x'+str(pos_y)
    pos_string_up = str(pos_x)+'x'+str(pos_y-1)
    pos_string_down = str(pos_x)+'x'+str(pos_y+1)

    if current in storage_dict and current not in visited_dict:
        depth = storage_dict[current]
        if depth < 9:
            visited_dict[current] = True
            counter += 1

    counter += check_for_next(pos_x, pos_y,-1, 0, storage_dict, visited_dict, counter, pos_string_left)
    counter += check_for_next(pos_x, pos_y,1, 0, storage_dict, visited_dict, counter, pos_string_right)
    counter += check_for_next(pos_x, pos_y,0, -1, storage_dict, visited_dict, counter, pos_string_up)
    counter += check_for_next(pos_x, pos_y,0, 1, storage_dict, visited_dict, counter, pos_string_down)
    
    return counter
    
def check_for_next(pos_x, pos_y, delta_x, delta_y, storage_dict, visited_dict, counter, pos_string):
    counter = 0
    if pos_string in storage_dict and pos_string not in visited_dict:
        depth = storage_dict[pos_string]
        if depth < 9:
            counter += recursive_mover(pos_x + delta_x, pos_y + delta_y, storage_dict, visited_dict)
    return counter

def problem_b(input_string, expected_result):
    """Problem A solved function
    """
    row_id = 0
    storage_dict = {}
    visited_dict = {}
    basins_found = {}
    for row in input_string.split('\n'):
        pos_id = 0
        for char in row:
            storage_dict[str(pos_id)+'x'+str(row_id)] = int(char)
            pos_id += 1
        row_id += 1

    row_id = 0
    for row in input_string.split('\n'):
        pos_id = 0
        for char in row:
            current = int(char)
            if str(pos_id-1)+'x'+str(row_id) in storage_dict:
                left = storage_dict[str(pos_id-1)+'x'+str(row_id)]
            else:
                left = 99

            if str(pos_id+1)+'x'+str(row_id) in storage_dict:
                right = storage_dict[str(pos_id+1)+'x'+str(row_id)]
            else:
                right = 99

            if str(pos_id)+'x'+str(row_id-1) in storage_dict:
                up = storage_dict[str(pos_id)+'x'+str(row_id-1)]
            else:
                up = 99

            if str(pos_id)+'x'+str(row_id+1) in storage_dict:
                down = storage_dict[str(pos_id)+'x'+str(row_id+1)]
            else:
                down = 99

            if (current < left) and (current < right) and (current < up) and current < down:
                #Calculate size of basin
                count = recursive_mover(pos_id, row_id, storage_dict, visited_dict)
                basins_found[str(pos_id)+'x'+str(row_id)] = count

            pos_id += 1
        row_id += 1
    
    my_values = sorted(list(basins_found.values()), reverse=True)[:3]

    solution = 1
    for value in my_values:
        solution = solution*value

    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)


problem_b(EXAMPLE_INPUT1, 1134)
problem_b(PROGBLEM_INPUT_TXT, 1327014)
print("\n")