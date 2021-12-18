"""
Template code
"""#import cmath for complex number operations
#from abc import abstractproperty
#import cmath
#import Path for file operations
from pathlib import Path

PROGBLEM_INPUT_TXT = Path("/Users/pergrapatin/Source/AOC2021/src/"\
    +"day17/input.txt").read_text()


def calculate_x_steps(start_x_vel):
    start_x = 0
    current_x_pos = start_x
    current_x_vel = start_x_vel
    pos_x_list = [start_x]
    while (current_x_vel != 0):
        current_x_pos += current_x_vel
        current_x_vel -= 1
        pos_x_list.append(current_x_pos)

    return pos_x_list

def calculate_y_steps(start_y_vel, min_y_target):
    start_y = 0
    current_y_pos = start_y
    current_y_vel = start_y_vel
    pos_y_list = [start_y]
    while current_y_pos > (min_y_target - 10):
        current_y_pos += current_y_vel
        current_y_vel -= 1
        pos_y_list.append(current_y_pos)
    return pos_y_list

def find_possible_xv(min_x_target, max_x_target):
    xv = {}
    for x_v in range(6, max_x_target+1):
        x_pos_list = calculate_x_steps(x_v)
        for value in x_pos_list:
            if min_x_target <= value <= max_x_target:
                if x_v in xv:
                    xv[x_v] += 1
                else:
                    xv[x_v] = 1
    return xv

def find_possible_yv(min_y_target, max_y_target):
    yv = {}
    for y_v in range(-120, 120):
        y_pos_list = calculate_y_steps(y_v, min_y_target)
        for value in y_pos_list:
            if min_y_target <= value <= max_y_target:
                if y_v in yv:
                    yv[y_v] += 1
                else:
                    yv[y_v] = 1
    return yv

def check_if_hit(xv, yv, min_x, max_x, min_y, max_y):
    x_pos = calculate_x_steps(xv)
    y_pos = calculate_y_steps(yv, min_y)
    for steps in range(max([len(x_pos),len(y_pos)])):
        x_step = steps
        y_step = steps
        if (steps > len(x_pos)-1):
            x_step = len(x_pos) - 1
        if (steps > len(y_pos) - 1):
            y_step = len(y_pos) - 1
        if min_x <= x_pos[x_step] <= max_x and min_y <= y_pos[y_step] <= max_y:
            return True
    return False


def problem_a(input_cords, expected_result):
    """Problem A solved function
    """
    min_x, max_x = input_cords[0][0],input_cords[0][1]
    min_y, max_y = input_cords[1][0],input_cords[1][1]

    xv_list = find_possible_xv(input_cords[0][0],input_cords[0][1])
    yv_list = find_possible_yv(input_cords[1][0],input_cords[1][1])

    count = 0

    for x_entry in xv_list:
        for y_entry in yv_list:
            if check_if_hit(x_entry, y_entry, min_x, max_x, min_y, max_y):
                count += 1

    solution = count
    
    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

problem_a([[20,30],[-10,-5]], 112)
problem_a([[235,259],[-118,-62]], 0)  #2294 too low
print("\n")
