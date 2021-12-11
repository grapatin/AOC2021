"""
Template code
"""#import cmath for complex number operations
#from abc import abstractproperty
#import cmath
#import Path for file operations
from pathlib import Path

PROGBLEM_INPUT_TXT = Path("/Users/pergrapatin/Source/AOC2021/src/"\
    +"day11/input.txt").read_text()

EXAMPLE_INPUT1 = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""
EXAMPLE_RESULT1 = 1656

def string_worker(input_string):
    """Helper string worker function
    """
    a_steps = input_string.split("\n")
    a_steps = [int(number) for number in input_string.split(',')]
    return a_steps

def string_maker(y,x):
    return str(y)+'x'+str(x)

def increase_all_around(pos_s, s_dict):
    row, pos = pos_s.split('x')

    for y in range(-1,2):
        for x in range(-1,2):
            t_row = int(row) + y
            t_pos = int(pos) + x
            str_t = string_maker(t_row, t_pos) 
            if str_t in s_dict:
                s_dict[str_t] += 1
    s_dict[pos_s] = -1000000


def problem_a(input_string, expected_result):
    """Problem A solved function
    """
    solution = 0
    rows = input_string.split('\n')

    storage_dict = {}
    row_id = 0
    for row in rows:
        pos = 0
        for char in row:
            storage_dict[string_maker(row_id, pos)] = int(char)
            pos += 1
        row_id += 1

    for time in range(100):
        for pos in storage_dict:
            storage_dict[pos] += 1
        
        cont = True
        while cont:
            cont = False
            for pos in storage_dict:
                if storage_dict[pos] > 9:
                    cont = True
                    increase_all_around(pos, storage_dict)
                
        for pos in storage_dict:
            if storage_dict[pos] < 0:
                solution += 1
                storage_dict[pos] = 0
    
    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

problem_a(EXAMPLE_INPUT1, EXAMPLE_RESULT1)
problem_a(PROGBLEM_INPUT_TXT, 1659)
print("\n")



def problem_b(input_string, expected_result):
    """Problem A solved function
    """
    solution = 0
    rows = input_string.split('\n')

    storage_dict = {}
    row_id = 0
    for row in rows:
        pos = 0
        for char in row:
            storage_dict[string_maker(row_id, pos)] = int(char)
            pos += 1
        row_id += 1

    for time in range(10000):
        for pos in storage_dict:
            storage_dict[pos] += 1
        
        cont = True
        while cont:
            cont = False
            for pos in storage_dict:
                if storage_dict[pos] > 9:
                    cont = True
                    increase_all_around(pos, storage_dict)
                
        all_f = True
        for pos in storage_dict:
            if storage_dict[pos] < 0:
                solution += 1
                storage_dict[pos] = 0
            else:
                all_f = False
        if all_f == True:
            solution = time+1
            break
    
    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

problem_b(EXAMPLE_INPUT1, 195)
problem_b(PROGBLEM_INPUT_TXT, 227)
print("\n")