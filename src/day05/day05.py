"""
Template code
"""#import cmath for complex number operations
#from abc import abstractproperty
#import cmath
#import Path for file operations
from os import SEEK_CUR
from pathlib import Path

PROGBLEM_INPUT_TXT = Path("/Users/pergrapatin/Source/AOC2021/src/"\
    +"day05/input.txt").read_text()

EXAMPLE_INPUT1 = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""
EXAMPLE_RESULT1 = 5

def string_builder(x1, y1):
    return str(x1) + 'x' + str(y1) + 'y'

def problem_a(input_string, expected_result):
    """Problem A solved function
    """
    rows = input_string.split('\n')
    storage_dict = {}

    for row in rows:
        start_stop = row.split(' -> ')
        x1 = int(start_stop[0].split(',')[0])
        y1 = int(start_stop[0].split(',')[1])
        x2 = int(start_stop[1].split(',')[0])
        y2 = int(start_stop[1].split(',')[1])
        if (x1 == x2):
            if y2 < y1:
                y1, y2 = y2, y1
            for ycord in range(y1, y2+1):
                search_strign = string_builder(x1, ycord)
                add_point(storage_dict, search_strign)
        if (y1 == y2):
            if x2 < x1:
                x1, x2 = x2, x1
            for xcord in range(x1, x2+1):
                search_strign = string_builder(xcord, y1)
                add_point(storage_dict, search_strign)

    solution = 0 
    for point in storage_dict:
        if storage_dict[point] > 1:
            solution += 1

    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

def add_point(storage_dict, search_strign):
    if search_strign in storage_dict:
        storage_dict[search_strign] += 1
    else:
        storage_dict[search_strign] = 1

def problem_b(input_string, expected_result):
    """Problem A solved function
    """
    rows = input_string.split('\n')
    storage_dict = {}

    for row in rows:
        start_stop = row.split(' -> ')
        x1 = int(start_stop[0].split(',')[0])
        y1 = int(start_stop[0].split(',')[1])
        x2 = int(start_stop[1].split(',')[0])
        y2 = int(start_stop[1].split(',')[1])
        if (x1 == x2):
            if y2 < y1:
                y1, y2 = y2, y1
            for ycord in range(y1, y2+1):
                search_string = string_builder(x1, ycord)
                add_point(storage_dict, search_string)
        elif (y1 == y2):
            if x2 < x1:
                x1, x2 = x2, x1
            for xcord in range(x1, x2+1):
                search_string = string_builder(xcord, y1)
                add_point(storage_dict, search_string)
        else:           
            #45 degree line
            if y2 < y1:
                y_delta = -1
            else:
                y_delta = 1
            if x2 < x1:
                x_delta = -1
            else:
                x_delta = 1
            diff = abs(x2 - x1)
            for delta in range(diff+1):
                search_string = string_builder(x1+(delta*x_delta), y1+(delta*y_delta))
                add_point(storage_dict, search_string)

    solution = 0 
    for point in storage_dict:
        if storage_dict[point] > 1:
            solution += 1

    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)



problem_a(EXAMPLE_INPUT1, EXAMPLE_RESULT1)
problem_a(PROGBLEM_INPUT_TXT, 5280)
print("\n")


problem_b(EXAMPLE_INPUT1, 12)
problem_b(PROGBLEM_INPUT_TXT, 16716)
