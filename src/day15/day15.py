"""
Template code
"""#import cmath for complex number operations
#from abc import abstractproperty
#import cmath
#import Path for file operations
from pathlib import Path
import sys

PROGBLEM_INPUT_TXT = Path("/Users/pergrapatin/Source/AOC2021/src/"\
    +"day15/input.txt").read_text()

EXAMPLE_INPUT1 = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""
EXAMPLE_RESULT1 = 40

def recursive_walker(current_pos, storage_dict, current_sum, visited_dict, target_pos):
    global best_result
    current_sum += storage_dict[current_pos]

    if current_pos not in visited_dict or current_sum < visited_dict[current_pos]:
        if (current_sum < best_result):
            visited_dict[current_pos] = current_sum
            if current_pos != target_pos: #still not there
                y = current_pos[0]
                x = current_pos[1]
                new_pos = (y+1,x)
                start_next_walk(storage_dict, current_sum, new_pos, visited_dict, target_pos)
                new_pos = (y,x+1)
                start_next_walk(storage_dict, current_sum, new_pos, visited_dict, target_pos)
                new_pos = (y,x-1)
                start_next_walk(storage_dict, current_sum, new_pos, visited_dict, target_pos)
                new_pos = (y-1,x)
                start_next_walk(storage_dict, current_sum, new_pos, visited_dict, target_pos)
            else:
                best_result = current_sum
                print('New best result found', best_result)
                pass

def start_next_walk(storage_dict, current_sum, new_pos, visited_dict, target_pos):
    if new_pos in storage_dict:
        recursive_walker(new_pos, storage_dict, current_sum, visited_dict, target_pos)

def problem_a(input_string, expected_result):
    """Problem A solved function
    """
    pos_x = pos_y = 0

    storage_dict = {}
    visited_dict = {}
    rows = input_string.split('\n')
    for row in rows:
        for char in row:
            storage_dict[(pos_y,pos_x)] = int(char)
            pos_x += 1
        pos_y += 1
        pos_x = 0
    
    current_pos = (0,0)
    target_pos = max(storage_dict)
    recursive_walker(current_pos, storage_dict, 0, visited_dict, target_pos)
    print_state(visited_dict, rows)


    solution = visited_dict[max(storage_dict)] - visited_dict[(0,0)]
    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

def print_state(visited_dict, rows):
    for y in range(len(rows)):
        for x in range(len(rows)):
            if (y, x) in visited_dict:
                print(visited_dict[(y,x)], end=' ')
            else:
                print('-', end='')
        print()

best_result = 9999999999999
sys.setrecursionlimit(50000)
problem_a(EXAMPLE_INPUT1, EXAMPLE_RESULT1)
#best_result = 9999999999
#problem_a(PROGBLEM_INPUT_TXT, 769)
print("\n")


def problem_b(input_string, expected_result):
    """Problem A solved function
    """
    pos_x = pos_y = 0

    storage_dict = {}
    visited_dict = {}
    rows = input_string.split('\n')
    for row in rows:
        for char in row:
            storage_dict[(pos_y,pos_x)] = int(char)
            pos_x += 1
        pos_y += 1
        pos_x = 0
    
    org_dict = storage_dict.copy()

    for l in range(1, 5):
        for pos in org_dict:
            y, x = pos[0], pos[1]
            y += pos_y*l
            number = storage_dict[pos] + l
            if number == 10:
                number = 1
            elif number == 11:
                number = 2
            elif number == 12:
                number = 3
            elif number == 13:
                number = 4
            elif number == 14:
                number = 5
            storage_dict[(y,x)] = number

    org_dict = storage_dict.copy()
    for l in range(1, 5):
        for pos in org_dict:
            y, x = pos[0], pos[1]
            x += pos_y*l
            number = storage_dict[pos] + l
            if number == 10:
                number = 1
            elif number == 11:
                number = 2
            elif number == 12:
                number = 3
            elif number == 13:
                number = 4
            elif number == 14:
                number = 5
            storage_dict[(y,x)] = number


    print_state(storage_dict, rows*5)
    current_pos = (0,0)
    target_pos = max(storage_dict)
    recursive_walker(current_pos, storage_dict, 0, visited_dict, target_pos)
    print_state(visited_dict, rows*5)


    solution = visited_dict[target_pos] - visited_dict[(0,0)]
    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)


best_result = 99999999999
sys.setrecursionlimit(50000)
problem_b(EXAMPLE_INPUT1, 315)
best_result = 4001
problem_b(PROGBLEM_INPUT_TXT, 0)
print("\n")
