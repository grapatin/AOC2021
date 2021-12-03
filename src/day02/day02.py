"""
Template code
"""#import cmath for complex number operations
#from abc import abstractproperty
#import cmath
#import Path for file operations
from pathlib import Path

PROGBLEM_INPUT_TXT = Path("/Users/pergrapatin/Source/AOC2021/src/"\
    +"day02/input.txt").read_text()

EXAMPLE_INPUT1 = """"""
EXAMPLE_RESULT1 = 1514

def string_worker(input_string):
    """Helper string worker function
    """
    a_steps = input_string.split("\n")
    return a_steps

def problem_a(input_string, expected_result):
    """Problem A solved function
    """

    rows = input_string.split('\n')

    depth = 0
    forward = 0

    for row in rows:
        number = int(row.split()[1])
        if 'forw' in row:
            forward += number
        elif 'up' in row:
            depth -= number
        else:
            depth += number

    solution = forward*depth

    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

def problem_b(input_string, expected_result):
    """Problem B solved function
    """

    rows = input_string.split('\n')

    aim = 0
    depth = 0
    forward = 0

    for row in rows:
        number = int(row.split()[1])
        if 'forw' in row:
            forward += number
            depth = depth +aim*number
        elif 'up' in row:
            aim -= number
        else:
            aim += number


    solution = forward*depth

    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

#problem_a(EXAMPLE_INPUT1, EXAMPLE_RESULT1)
problem_a(PROGBLEM_INPUT_TXT, 0)
print("\n")
problem_b(PROGBLEM_INPUT_TXT, 0)

