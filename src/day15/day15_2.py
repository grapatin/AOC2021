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

def recursive_walker(current_pos, storage_dict, current_sum, visited_dict, target_pos, max_value):
    global best_result
    current_sum += storage_dict[current_pos]

    if current_pos not in visited_dict or current_sum < visited_dict[current_pos]:
        if (current_sum < max_value):
            visited_dict[current_pos] = current_sum
            if current_pos != target_pos: #still not there
                y = current_pos[0]
                x = current_pos[1]
                new_pos = (y+1,x)
                start_next_walk(storage_dict, current_sum, new_pos, visited_dict, target_pos, max_value)
                new_pos = (y,x+1)
                start_next_walk(storage_dict, current_sum, new_pos, visited_dict, target_pos, max_value)
                new_pos = (y,x-1)
                start_next_walk(storage_dict, current_sum, new_pos, visited_dict, target_pos, max_value)
                new_pos = (y-1,x)
                start_next_walk(storage_dict, current_sum, new_pos, visited_dict, target_pos, max_value)
            else:
                max_value = current_sum
                pass

def start_next_walk(storage_dict, current_sum, new_pos, visited_dict, target_pos, max_value):
    if new_pos in storage_dict:
        recursive_walker(new_pos, storage_dict, current_sum, visited_dict, target_pos, max_value)



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
    target_pos = (1,0)
    max_value = 40
    recursive_walker(current_pos, storage_dict, 0, visited_dict, (1,0), max_value)
    recursive_walker(current_pos, storage_dict, 0, visited_dict, (0,1))
    recursive_walker((1,0), storage_dict, visited_dict[(1,0)], visited_dict, (2,0))
    recursive_walker((0,1), storage_dict, visited_dict[(0,1)], visited_dict, (2,0))
    # recursive_walker(current_pos, storage_dict, 0, visited_dict, (2,0))

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
                print('- ', end='')
        print()

best_result = 9999999999999
sys.setrecursionlimit(50000)
problem_a(EXAMPLE_INPUT1, EXAMPLE_RESULT1)
best_result = 777
problem_a(PROGBLEM_INPUT_TXT, 769)
print("\n")
